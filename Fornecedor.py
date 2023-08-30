# import paho.mqtt.client as mqtt

# Configuração do cliente
# client = mqtt.Client()
# client.connect("localhost", 1883, 60)  # Conectando ao broker em localhost na porta padrão 1883

# Publica uma mensagem
# client.publish("meu/topico", "Olá, MQTT!")
# Desconecta
# client.disconnect()

from ClasseFornecedor import Fornecedor

import paho.mqtt.client as mqtt

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

    #Com essa mensagem, o fornecedor tem que enviar o produto pro almoxarifado

    #TODO


# Configuração básica
fornecedor = Fornecedor(1)
fornecedor.liberar_produto(1, 10)
broker_address = "localhost"
port = 1883

# O nome foi alterado para refletir que ele pode ser tanto publisher quanto subscriber.
client = mqtt.Client("Client1")
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)

client.loop_forever()
