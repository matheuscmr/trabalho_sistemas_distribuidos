import paho.mqtt.client as mqtt
import time
from ClasseEstoque import Estoque

def on_connect(client, userdata, flags, rc):
    meu_estoque = userdata
    client.subscribe("estoque/fabrica")

def on_message(client, userdata, message):
    meu_estoque = userdata
    print(f"Mensagem de resposta recebida: {message.payload.decode()} no tópico {message.topic}")
    mensagem, valor = message.payload.decode().split()

    if mensagem == "estoque":
        novo_estoque = int(valor)
        meu_estoque.add_Estoque(novo_estoque)

        if meu_estoque.get_Estoque() >= meu_estoque.get_Pedidos():
            print("Demanda cumprida")
            meu_estoque.remove_Estoque(meu_estoque.get_Pedidos())
            meu_estoque.remove_Pedidos(meu_estoque.get_Pedidos())
            
        print("Produtos a serem produzidos:", meu_estoque.get_Pedidos())
        print("Estoque atual:", meu_estoque.get_Estoque())

# Configuração básica
estoque = Estoque()
broker_address = "localhost"
port = 1883
topic = "test/topic"

estoque.add_Pedidos(4)
client = mqtt.Client(userdata=estoque)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port)

print("Conectado ...")
print("Pedidos iniciais:", estoque.get_Pedidos())

time.sleep(5)

if estoque.get_Pedidos() > estoque.get_Estoque():
    print("Pedido maior que o número em estoque...")
    produtos_a_produzir = estoque.get_Pedidos() - estoque.get_Estoque()
    print(f"Solicitando à fábrica que {produtos_a_produzir} novos produtos sejam enviados ...")
    client.publish("fabrica/estoque", "produzir " + str(produtos_a_produzir))  # publicação no tópico correto
client.loop_forever()
