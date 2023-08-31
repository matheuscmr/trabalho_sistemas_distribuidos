from ClasseAlmoxarifado import Almoxarifado
import paho.mqtt.client as mqtt

def enviar_material(client, almoxarifado, quantidade):  # Adicionei a quantidade como argumento
    print("Função enviar material executada!")
    almoxarifado.remove_estoque(quantidade)
    mensagem = f"envio {quantidade}"
    print(mensagem)
    client.publish("fabrica/almoxarifado", mensagem)
    almoxarifado.set_fprodutos(almoxarifado.get_fprodutos() - quantidade)

def solicita_fornecedor(client, almoxarifado, qdd):
    print("Função solicitar fornecedor executada!")
    mensagem = f"fornecedor {qdd}"
    print(mensagem)
    client.publish("almoxarifado/fornecedor", mensagem)

def on_connect(client, userdata, flags, rc):
    print("Conectado com sucesso!")
    client.subscribe("fabrica/almoxarifado")
    client.subscribe("almoxarifado/fornecedor")

def on_message(client, userdata, message):
    almoxarifado = userdata
    print(f"Mensagem recebida: {message.payload.decode()} no tópico {message.topic}")
    mensagem, qtd = message.payload.decode().split()
    qtd = int(qtd)

    if mensagem == "solicita":
        if almoxarifado.get_estoque() >= qtd:
            enviar_material(client, almoxarifado, qtd)
        else:
            print("solicitar ao fonecedor")
            solicita_fornecedor(client, almoxarifado, qtd - almoxarifado.get_estoque())

    elif mensagem == "envio":  # Esta é a resposta do fornecedor
        almoxarifado.add_estoque(qtd)
        print(f"Adicionado ao estoque: {qtd}")

# Configuração básica
almoxarifado = Almoxarifado()
print("so passei aqui uma vez")
almoxarifado.add_estoque(10)
broker_address = "localhost"
port = 1883

client = mqtt.Client(userdata=almoxarifado)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)
client.loop_forever()
