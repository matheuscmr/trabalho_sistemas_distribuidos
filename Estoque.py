import paho.mqtt.client as mqtt

# Callback quando uma mensagem é recebida
def on_message(client, userdata, msg):
    print(f"Recebido: {msg.topic} -> {msg.payload.decode('utf-8')}")

# Configuração do cliente
client = mqtt.Client()
client.connect("localhost", 1883, 60)  # Conectando ao broker em localhost na porta padrão 1883
client.subscribe("meu/topico")
client.on_message = on_message

# Mantém o cliente ouvindo indefinidamente
client.loop_forever()