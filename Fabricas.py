import paho.mqtt.client as mqtt

# Configuração do cliente
client = mqtt.Client()
client.connect("localhost", 1883, 60)  # Conectando ao broker em localhost na porta padrão 1883

# Publica uma mensagem
client.publish("meu/topico", "Olá, MQTT!")
print("teste")
# Desconecta
client.disconnect()