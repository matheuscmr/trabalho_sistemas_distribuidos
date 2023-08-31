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
    print("Função envia estoque executada!") # print que mostra que função foi chamada
    produtos = fabrica1.get_linha_p(1) # pega os produtos finalizados da linha 1
    mensagem = "estoque "+str(produtos[1]) #enviao produto 1 da linha 1
    print(mensagem) # imprime pra ver se esta enviando correto
    fabrica1.enviar_produtos(1, 1) #envia todos os produtos da linha 1 do tipo 1

    client.publish("resposta/topico", mensagem) # envio da mensagem

# Callback quando conectado.

def solicita_material():  # função que solicita material
    print("Função solicita material executada!") # print pra ver se a função foi chamda
    mensagem = "solicita "+ str(fabrica1.QuantidadeParaFabricar[1]) # solicita x * o numero de produtos que eu quero fabricar
    print(mensagem)
    client.publish("resposta/topico", mensagem)


def on_connect(client, userdata, flags, rc):
    print("Conectado com o código:", rc)
    client.subscribe("test/topic")

# Callback quando uma mensagem é recebida.


def on_message(client, userdata, message):
    print(f"Mensagem recebida: {message.payload.decode()} no tópico {message.topic}")
    mensagem = message.payload.decode()
    tipo, quantidade = mensagem.split()
    quantidade = int(quantidade) # a variavel quantidade sinaliza a quantidade a ser produzida
    # Se a mensagem recebida for "executar_funcao", execute a função.
    if tipo == "produzir": # se for produzir ...
        produtos = fabrica1.get_linha_p(1) # pega a quantidade de produtos finalizados na linha 1
        if quantidade >= produtos[1]: # se a quantidade a ser produzida for maior do que oque tem finalizado...
            quantidade = quantidade - produtos[1]
            fabrica1.adicionar_quantidade(1, int(quantidade)) #retira a quantidade de produtos a serem produzidos
            print("recebido do estoque pedido de produção")
            print("pedido de produção :")
            print(fabrica1.get_quantidade_p(1))
        envia_estoque() # no fim ela envia o estoque
    if(fabrica1.get_quantidade_p(1) >= 0): # se ainda exister produtos a serem fabricados
        terminou = False
        while terminou == False:
            erro = fabrica1.fabricar_produto() # tenta fabricar produto, se der erro, acabou o material
            if (erro == "error"): # se der erro, solita o material
                solicita_material()
            materiais = fabrica1.get_linha_m(1)
            if(fabrica1.get_quantidade_p(1) == materiais[1] + 3): #sai do laço quando tiver ao menos 3 materiais a mais do que a quantidade de produtos a serem fabricado
                terminou == True
        while(fabrica1.fabricar_produto() != "erro"): #fabrica o que tem pra fabricar
            print("produto fabricado")
        envia_estoque() # enviar de novo o estoque se tiver algo
    envia_estoque() # enviar de novo o estoque se tiver algo

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
