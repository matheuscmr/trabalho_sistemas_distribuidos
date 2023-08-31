# import paho.mqtt.client as mqtt

# Configuração do cliente
# client = mqtt.Client()
# client.connect("localhost", 1883, 60)  # Conectando ao broker em localhost na porta padrão 1883

# Publica uma mensagem
# client.publish("meu/topico", "Olá, MQTT!")
# Desconecta
# client.disconnect()

from ClasseAlmoxarifado import Almoxarifado

import paho.mqtt.client as mqtt


def enviar_material():
    print("Função enviar material executada!")
    quantidade = almoxarifado.get_estoque()
    almoxarifado.remove_estoque(quantidade)
    mensagem = "envio "+ str(quantidade) # solicita x * o numero de produtos que eu quero fabricar
    print(mensagem)
    client.publish("resposta/topico", mensagem)
    almoxarifado.set_fprodutos((almoxarifado.get_fprodutos() - quantidade))


def solicita_fornecedor(qdd):
    print("Função solicitar fornecedor executada!")
    mensagem = "fornecedor "+ qdd # solicita x * o numero de produtos que eu quero fabricar
    print(mensagem)
    client.publish("resposta/topico", mensagem)

# Callback quando conectado.
def on_connect(client, userdata, flags, rc):
    print("Conectado com o código:", rc)
    client.subscribe("test/topic")

# Callback quando uma mensagem é recebida.
def on_message(client, userdata, message):
    print(
        f"Mensagem recebida: {message.payload.decode()} no tópico {message.topic}")
    mensagem = message.payload.decode()
    tipo, quantidade = mensagem.split()
    quantidade = int(quantidade)
    if(tipo == "solicita"):
        if(almoxarifado.get_estoque()>= int(quantidade)):
            enviar_material()
        else:
            solicita_fornecedor(3 + almoxarifado.get_fprodutos)


    #Com essa mensagem, o almoxarifado tem que fazer o pedido de peças para o forncecedor

    #TODO

# Configuração básica
almoxarifado = Almoxarifado(1)
broker_address = "localhost"
port = 1883
almoxarifado.add_estoque(10)
# O nome foi alterado para refletir que ele pode ser tanto publisher quanto subscriber.
client = mqtt.Client("Client1")
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)

client.loop_forever()
