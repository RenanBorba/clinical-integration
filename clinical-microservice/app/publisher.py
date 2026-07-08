# Cliente Python para comunicação com o RabbitMQ
import pika
# Importa variáveis do arquivo config.py
from app.config import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    QUEUE_NAME
)

def publish(message: str):
    # Processa uma mensagem por vez
    connection = pika.BlockingConnection(
    # Inicializa conexão com RabbitMQ
    pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT
    ))
    # Abre o canal
    channel = connection.channel()
    # Declara uma fila
    channel.queue_declare(
        queue=QUEUE_NAME,
        durable=True
    )

    # Não envia mais de 1 mensagem por vez. 
    # Só vai mandar a próxima quando terminar e confirmar a atual
    channel.basic_qos(prefetch_count=1)

    # Declara um publish
    channel.basic_publish(
        # Declara a exchange, está vazia "" para utilizar a default exchange, 
        # sem a necessidade de definição
        exchange="",
        # Declara a routing key conforme o nome da fila
        routing_key=QUEUE_NAME,
        # Body conforme a definição de message como string
        body=message,
        properties=pika.BasicProperties(
            # Foca na entrega garantida da mensagem
            delivery_mode=2
        )
    )

    connection.close()