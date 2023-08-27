import paho.mqtt.client as mqtt

# Callback quando conectado.
def on_connect(client, userdata, flags, rc):
    print("Conectado com o código:", rc)
    client.subscribe("resposta/topico")  # Assina o tópico de resposta

# Callback quando uma mensagem é recebida.
def on_message(client, userdata, message):
    print(f"Mensagem de resposta recebida: {message.payload.decode()} no tópico {message.topic}")
    mensagens = message.payload.decode()
    mensagem, tipo,valor = mensagens.split()
    if mensagem == "estoque":
        EstoqueP[int(tipo)] = EstoqueP[int(tipo)]+ int(valor)
    print("estoque atual :")
    print(EstoqueP)

# Configuração básica
EstoqueP = []
for i in range(5):
    EstoqueP.append(0)
broker_address = "localhost"
port = 1883
topic = "test/topic"

client = mqtt.Client("PublisherSubscriber")  # Instância do cliente com um nome que reflete suas duas funções
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)

# Publica uma mensagem
client.publish(topic, "executar_funcao")

client.loop_forever()  # Mantém o cliente ouvindo por mensagens no tópico "resposta/topico"
