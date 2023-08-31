from ClasseAlmoxarifado import Almoxarifado
import paho.mqtt.client as mqtt

def enviar_material(client, almoxarifado):
    print("Função enviar material executada!")
    quantidade = almoxarifado.get_estoque()
    almoxarifado.remove_estoque(quantidade)
    mensagem = f"envio {quantidade}"
    print(mensagem)
    client.publish("fabrica/almoxarifado", mensagem)
    almoxarifado.set_fprodutos(almoxarifado.get_fprodutos() - quantidade)

def solicita_fornecedor(client, almoxarifado, qdd):
    print("Função solicitar fornecedor executada!")
    mensagem = f"fornecedor {qdd}"
    print(mensagem)
    client.publish("almoxarifado/fornecedor", mensagem)  # Tópico para solicitar material ao fornecedor

def on_connect(client, userdata, flags, rc):
    print("Conectado com sucesso!")
    client.subscribe("fabrica/almoxarifado")
    client.subscribe("fornecedor/almoxarifado/resposta")  # Tópico para receber resposta do fornecedor

def on_message(client, userdata, message):
    almoxarifado = userdata
    print(f"Mensagem recebida: {message.payload.decode()} no tópico {message.topic}")
    mensagem, quantidade = message.payload.decode().split()
    quantidade = int(quantidade)

    if mensagem == "solicita":
        if almoxarifado.get_estoque() >= quantidade:
            enviar_material(client, almoxarifado)
        else:
            solicita_fornecedor(client, almoxarifado, 3 + almoxarifado.get_fprodutos)

    elif mensagem == "envio":  # Esta é a resposta do fornecedor
        almoxarifado.add_estoque(quantidade)
        print(f"Adicionado ao estoque: {quantidade}")

# Configuração básica
almoxarifado = Almoxarifado(1)
broker_address = "localhost"
port = 1883
almoxarifado.add_estoque(10)

client = mqtt.Client(userdata=almoxarifado)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)
client.loop_forever()
