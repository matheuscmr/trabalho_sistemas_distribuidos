import paho.mqtt.client as mqtt
import random
import time
from ClasseEstoque import Estoque

# Callback quando conectado.


def on_connect(client, userdata, flags, rc):
    print("Conectado com o código:", rc)
    client.subscribe("resposta/topico")  # Assina o tópico de resposta

# Callback quando uma mensagem é recebida.


def on_message(client, userdata, message):
    print(
        f"Mensagem de resposta recebida: {message.payload.decode()} no tópico {message.topic}")
    mensagens = message.payload.decode()
    mensagem, tipo, valor = mensagens.split()
    if mensagem == "estoque":
        estoque.add_Estoque(estoque.get_Estoque() + int(valor))
        if estoque.get_Estoque() >= estoque.get_Pedidos():
            estoque.remove_Estoque(estoque.get_Pedidos())
            estoque.remove_Pedidos(estoque.get_Pedidos())
        else:
            print("pedido maior que o estoque ...")
            estoque.remove_Pedidos(estoque.get_Estoque())
            estoque.remove_Estoque(estoque.get_Estoque())
        print("estoque atual :")
        print(estoque.get_Estoque())


def gerar_pedidos():  # função que provisoriamente ira gerar um número de pedidos do produto 1
    return random.randint(1, 30)


# Configuração básica
estoque = Estoque()
broker_address = "localhost"
port = 1883
topic = "test/topic"
# Instância do cliente com um nome que reflete suas duas funções
client = mqtt.Client("PublisherSubscriber")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port)
print("conectado ...")
estoque.add_Pedidos(3)
time.sleep(3)
if (estoque.get_Pedidos() > estoque.get_Estoque()):
    print("pedido maior que o numero em estoque...")
    estoque.remove_Pedidos(estoque.get_Pedidos() -  estoque.get_Estoque())
    estoque.remove_Estoque(estoque.get_Estoque())
    print("solicitando a fabrica que novos produtos sejam enviados ...")
    client.publish(topic, "produzir "+str(estoque.get_Pedidos()))
else:
    estoque.remove_Produtos(estoque.get_Produtos() - estoque.get_Pedidos())
    estoque.remove_Pedidos(estoque.get_Pedidos())
    print(pedidosT, " produtos removidos do estoque")
# Publica uma mensagem
# Mantém o cliente ouvindo por mensagens no tópico "resposta/topico"
client.loop_forever()
