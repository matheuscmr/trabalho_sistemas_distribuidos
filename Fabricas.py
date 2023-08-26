#import paho.mqtt.client as mqtt

# Configuração do cliente
#client = mqtt.Client()
#client.connect("localhost", 1883, 60)  # Conectando ao broker em localhost na porta padrão 1883

# Publica uma mensagem
#client.publish("meu/topico", "Olá, MQTT!")
# Desconecta
#client.disconnect()

from ClasseFabrica import Fabrica

fabrica1 = Fabrica(2)
print(fabrica1.get_id())
print(fabrica1.get_linhas())
fabrica1.inserir_material(1,1)
fabrica1.inserir_material(1,1)
fabrica1.inserir_material(1,2)
fabrica1.inserir_material(1,2)
print(fabrica1.get_linhas())
