# Usa uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR ./

# Atualiza a lista de pacotes e instala as ferramentas necessárias.
# Em seguida, instala a biblioteca paho-mqtt para Python.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && pip install paho-mqtt \
    && apt install mosquitto mosquitto-clients -y --no-install-recommends


# Define o comando padrão a ser executado
CMD ["python", "-c", "print('Olá, Docker com MQTT!')"]