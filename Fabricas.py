from ClasseFabrica import Fabrica
import paho.mqtt.client as mqtt

def envia_estoque(client, fabrica1):  
    print("Função envia estoque executada!")
    produtos = fabrica1.get_linha_p(1)
    mensagem = "estoque "+str(produtos[1])
    print(mensagem)
    fabrica1.enviar_produtos(1, 1)
    client.publish("estoque/fabrica", mensagem)

def solicita_material(client):  
    print("Função solicita material executada!")
    mensagem = "solicita "+str(fabrica1.QuantidadeParaFabricar[1])
    print(mensagem)
    client.publish("fabrica/almoxarifado", mensagem)

def on_connect(client, userdata, flags, rc):
    print("Conectado com o código:", rc)
    client.subscribe("fabrica/estoque")  # assinatura do tópico correto
    
def on_message(client, userdata, message):
    fabrica1 = userdata
    print(f"Mensagem recebida: {message.payload.decode()} no tópico {message.topic}")
    tipo, quantidade = message.payload.decode().split()
    quantidade = int(quantidade)
    
    if tipo == "produzir":
        produtos = fabrica1.get_linha_p(1)
        if quantidade >= produtos[1]:
            quantidade -= produtos[1]
            fabrica1.adicionar_quantidade(1, quantidade)
            envia_estoque(client, fabrica1)

        while fabrica1.get_quantidade_p(1) > 0 and fabrica1.fabricar_produto(1, 1) != "erro":
            pass

        solicita_material(client)
        envia_estoque(client, fabrica1)

# Configuração básica
fabrica1 = Fabrica(1)
fabrica1.adicionar_produtos(1, 1, 5)
broker_address = "localhost"
port = 1883

client = mqtt.Client(userdata=fabrica1)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)
client.loop_forever()
