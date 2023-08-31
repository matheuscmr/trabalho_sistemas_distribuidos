from ClasseAlmoxarifado import Almoxarifado
import paho.mqtt.client as mqtt

def enviar_material(client, almoxarifado):
    print("Função enviar material executada!")
    quantidade = almoxarifado.get_estoque()
    almoxarifado.remove_estoque(quantidade)
    mensagem = "envio "+ str(quantidade)
    print(mensagem)
    client.publish("fabrica/almoxarifado", mensagem)
    almoxarifado.set_fprodutos(almoxarifado.get_fprodutos() - quantidade)

def solicita_fornecedor(client, qdd):
    print("Função solicitar fornecedor executada!")
    mensagem = "fornecedor "+ qdd
    print(mensagem)
    client.publish("fabrica/almoxarifado", mensagem)

def on_connect(client, userdata, flags, rc):
    client.subscribe("fabrica/almoxarifado")

def on_message(client, userdata, message):
    almoxarifado = userdata
    print(f"Mensagem recebida: {message.payload.decode()} no tópico {message.topic}")
    mensagem = message.payload.decode()
    tipo, quantidade = mensagem.split()
    quantidade = int(quantidade)
    if tipo == "solicita":
        if almoxarifado.get_estoque() >= quantidade:
            enviar_material(client, almoxarifado)
        else:
            solicita_fornecedor(client, 3 + almoxarifado.get_fprodutos)

# Configuração básica
almoxarifado = Almoxarifado(1)
broker_address = "localhost"
port = 1883
almoxarifado.add_estoque(10)

client = mqtt.Client(userdata=almoxarifado)  # Passar almoxarifado como userdata
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)
client.loop_forever()
