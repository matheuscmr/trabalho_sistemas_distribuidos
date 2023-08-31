# import paho.mqtt.client as mqtt

# Configuração do cliente
# client = mqtt.Client()
# client.connect("localhost", 1883, 60)  # Conectando ao broker em localhost na porta padrão 1883

# Publica uma mensagem
# client.publish("meu/topico", "Olá, MQTT!")
# Desconecta
# client.disconnect()

from ClasseFabrica import Fabrica

import paho.mqtt.client as mqtt


def envia_estoque():  # teste de envio de estoque do produto 1 da linha 1
    print("Função envia estoque executada!")
    produtos = fabrica1.get_linha_p(1)
    mensagem = "estoque 1 "+str(produtos[1])
    print(mensagem)
    fabrica1.enviar_produtos(1, 1)

    client.publish("resposta/topico", mensagem)

# Callback quando conectado.

def solicita_material():  # teste de envio de estoque do produto 1 da linha 1
    print("Função solicita material executada!")
    mensagem = "solicita "+ str(fabrica1.QuantidadeParaFabricar[1]) # solicita x * o numero de produtos que eu quero fabricar
    print(mensagem)
    client.publish("resposta/topico", mensagem)


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
    # Se a mensagem recebida for "executar_funcao", execute a função.
    if tipo == "produzir":
        produtos = fabrica1.get_linha_p(1)
        if quantidade >= produtos[1]:
            quantidade = quantidade - produtos[1]
            fabrica1.adicionar_quantidade(1, int(quantidade))
            print("recebido do estoque pedido de produção")
            print("pedido de produção :")
            print(fabrica1.get_quantidade_p(1))
    envia_estoque()


# Configuração básica
fabrica1 = Fabrica(1)
fabrica1.adicionar_produtos(1, 1, 5)
broker_address = "localhost"
port = 1883

# O nome foi alterado para refletir que ele pode ser tanto publisher quanto subscriber.
client = mqtt.Client("Client1")
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)

client.loop_forever()
