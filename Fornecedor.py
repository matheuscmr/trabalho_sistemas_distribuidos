import paho.mqtt.client as mqtt

# Assumindo que o fornecedor tenha recursos ilimitados para enviar para o almoxarifado.
def envia_material_para_almoxarifado(client, quantidade):
    print(f"Enviando {quantidade} materiais para o almoxarifado!")
    client.publish("fornecedor/almoxarifado/resposta", f"envio {quantidade}")

def on_connect(client, userdata, flags, rc):
    print("Conectado com sucesso!")
    client.subscribe("almoxarifado/fornecedor")

def on_message(client, userdata, message):
    print(f"Mensagem recebida: {message.payload.decode()} no tópico {message.topic}")
    mensagem, quantidade = message.payload.decode().split()
    quantidade = int(quantidade)

    if mensagem == "fornecedor":
        envia_material_para_almoxarifado(client, quantidade)

broker_address = "localhost"
port = 1883

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)
client.loop_forever()
