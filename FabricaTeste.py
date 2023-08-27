#import paho.mqtt.client as mqtt

# Configuração do cliente
#client = mqtt.Client()
#client.connect("localhost", 1883, 60)  # Conectando ao broker em localhost na porta padrão 1883

# Publica uma mensagem
#client.publish("meu/topico", "Olá, MQTT!")
# Desconecta
#client.disconnect()

from ClasseFabrica import Fabrica

fabrica1 = Fabrica(1)
print(" id da frabrica")
print(fabrica1.get_id())
print("linhas de materias:")
print(fabrica1.get_linhas_m())
for i in range(10):
    fabrica1.inserir_material(1,i)
fabrica1.inserir_material(1,1)
fabrica1.inserir_material(1,2)
fabrica1.inserir_material(1,2)
print("linhas de materias apos adicionados")
print(fabrica1.get_linhas_m())
print("lista do material 1")
print(fabrica1.get_material(1))

fabrica1.adicionar_quantidade(1,2)
print("produtos a serem fabricados")
print(fabrica1.get_quantidade())

fabrica1.fabricar_produto(1,1)
print(fabrica1.get_linhas_m())
print(fabrica1.get_linhas_p())
fabrica1.enviar_produto(1,1)
print("produtos a serem fabricados")
print(fabrica1.get_quantidade())