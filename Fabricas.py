from ClasseFabrica import Fabrica
import paho.mqtt.client as mqtt
import time

def envia_estoque(client, fabrica1):  # função que realiza o envio de estoque, recebe o objeto fabrica1 
    print("Função envia estoque executada!") # print para verificar se entrou na função
    produtos = fabrica1.get_linha_p(1) # get linha p retorna todos os produtos da linha
    mensagem = "estoque "+str(produtos[1]) # aqui no caso, produtos[1] seria a quantidade de produtos 1
    print(mensagem) # imprime a mensagem pra ver se esta tudo certo
    fabrica1.enviar_produtos(1, 1) # envia todos os produtos do tipo 1 que estiverem na linha
    client.publish("fabrica/estoque", mensagem) # envia a mensagem para estoque, funciona mesmo se nao tiver produto


def solicita_material(client, fabrica1, quantidade):  #função para solicitar material
    print("Função solicita material executada!") # print para verificar se pelo menos entrou na funçãp
    mensagem = "solicita "+str(quantidade) #solicita a quantidade que mandou na função
    print(mensagem) # imprime para ver se esta correto
    client.publish("fabrica/almoxarifado", mensagem) # envia a e mensagem

def on_connect(client, userdata, flags, rc):
    print("Conectado com o código:", rc)
    client.subscribe("fabrica/estoque")  # conexao fabrica estoque
    client.subscribe("fabrica/almoxarifado") # conexao fabrica almoxarifado
    
def on_message(client, userdata, message):
    fabrica1 = userdata
    print(f"Mensagem recebida: {message.payload.decode()} no tópico {message.topic}")
    tipo, quantidade = message.payload.decode().split()
    quantidade = int(quantidade)

    if tipo == "produzir": # se a mensagem for uma mensagem para produzir
        produtos = fabrica1.get_linha_p(1) # pegar os produtos da linha

        # Se há produtos já fabricados, envie-os primeiro.
        if produtos[1] > 0:
            envia_estoque(client, fabrica1) # envia os produtos

        # Tente fabricar os produtos
        for _ in range(quantidade):
            time.sleep(2)
            status = fabrica1.fabricar_produto(1, 1)

            # Se fabricado com sucesso, reduza a quantidade solicitada
            if status != "error":
                quantidade -= 1

            # Se houve um erro e não há material suficiente, solicite materiais
            elif fabrica1.material_suficiente(1) == False:
                solicitacao = quantidade - fabrica1.get_material_disponivel(1)
                solicita_material(client, fabrica1, solicitacao)
                break

        # Se todos os produtos forem fabricados, envie ao estoque
        if quantidade == 0:
            envia_estoque(client, fabrica1)

    elif tipo == "envio": #mensagem que recebe do almoxarifado
        fabrica1.inserir_materiais(1, 1, quantidade) # insere os materias na linha 1

        # Tente fabricar novamente com os novos materiais
        produtos = fabrica1.get_linha_p(1)
        for _ in range(produtos[1]):
            time.sleep(2)
            fabrica1.fabricar_produto(1, 1)

        envia_estoque(client, fabrica1)


# Configuração básica
fabrica1 = Fabrica(1)
fabrica1.adicionar_produtos(1, 1, 5) # começa com 5 produtos na linha
broker_address = "localhost"
port = 1883

client = mqtt.Client(userdata=fabrica1)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)
client.loop_forever()
