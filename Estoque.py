import paho.mqtt.client as mqtt
import time
from ClasseEstoque import Estoque
import threading

def on_connect(client, userdata, flags, rc):
    meu_estoque = userdata
    client.subscribe("fabrica/estoque")


def monitorar_estoque(meu_estoque, client):
    """
    Monitora o estoque e determina a cor (vermelho, amarelo ou verde) com base na quantidade.
    """
    if meu_estoque.get_Estoque() <= 3:
        print("Estoque em VERMELHO!")
        # Se estiver em vermelho, solicitar produtos para chegar ao amarelo (5 produtos)
        produtos_a_produzir = 5 - meu_estoque.get_Estoque()
        print(f"Solicitando à fábrica que {produtos_a_produzir} novos produtos sejam enviados para sair do estado VERMELHO...")
        client.publish("fabrica/estoque", "produzir " + str(produtos_a_produzir))
    elif 3 < meu_estoque.get_Estoque() <= 5:
        print("Estoque em AMARELO!")
    elif meu_estoque.get_Estoque() >= 10:
        print("Estoque em VERDE!")
    else:
        print("Estoque entre AMARELO e VERDE!")



def on_message(client, userdata, message):
    meu_estoque = userdata
    print(f"Mensagem de resposta recebida: {message.payload.decode()} no tópico {message.topic}")
    mensagem, valor = message.payload.decode().split()

    if mensagem == "estoque": #mensagem que recebe da fabrica, que repoe os produtos
        novo_estoque = int(valor)
        meu_estoque.add_Estoque(novo_estoque) # repoe os produtos

        # Atende aos pedidos usando o novo estoque
        if meu_estoque.get_Pedidos() > 0:
            quantidade_atendida = min(meu_estoque.get_Estoque(), meu_estoque.get_Pedidos())
            meu_estoque.remove_Estoque(quantidade_atendida)
            meu_estoque.remove_Pedidos(quantidade_atendida)
            print(f"Atendidos {quantidade_atendida} pedidos usando o novo estoque.")

        # Verifica se ainda há pedidos pendentes
        if meu_estoque.get_Pedidos() > 0:
            produtos_a_produzir = meu_estoque.get_Pedidos()
            print(f"Solicitando à fábrica que {produtos_a_produzir} novos produtos sejam enviados ...")
            client.publish("fabrica/estoque", "produzir " + str(produtos_a_produzir))

        print("Produtos a serem produzidos:", meu_estoque.get_Pedidos())
        print("Estoque atual:", meu_estoque.get_Estoque())

        # Chamar a função para monitorar o estoque depois de processar a mensagem
        monitorar_estoque(meu_estoque, client)





def request_products(client, estoque): # função para usar em thread para sempre solicitar novos produtos
    while True:
        try:
            produtos_desejados = int(input("Informe a quantidade de produtos desejados: "))
            estoque.add_Pedidos(produtos_desejados)
            print("Pedidos totais:", estoque.get_Pedidos())

            time.sleep(2) 

            if estoque.get_Pedidos() > estoque.get_Estoque():
                print("Pedido maior que o número em estoque...")
                produtos_a_produzir = estoque.get_Pedidos() - estoque.get_Estoque()
                print(f"Solicitando à fábrica que {produtos_a_produzir} novos produtos sejam enviados ...")
                client.publish("fabrica/estoque", "produzir " + str(produtos_a_produzir))

        except ValueError:
            print("Por favor, insira um número válido.")
        except KeyboardInterrupt:
            print("\nEncerrando o programa...")
            client.disconnect()
            break

# Configuração básica
estoque = Estoque()
broker_address = "localhost"
port = 1883

client = mqtt.Client(userdata=estoque)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port)

threading.Thread(target=client.loop_forever).start()
threading.Thread(target=request_products, args=(client, estoque)).start()
