import json
import time
import pika

from app.config import (
    RABBITMQ_HOST,
    QUEUE_NAME
)

from app.database import Database
from app.fhir_service import FHIRService
from app.mapper import (
    map_patient,
    map_event_to_fhir
)

fhir = FHIRService()

def callback(ch, method, properties, body):
    """
    Processa uma mensagem recebida da fila RabbitMQ.
    """

    try:

        event = json.loads(body.decode())

        print(f"\nEvento recebido:\n{event}")

        # Consulta os dados do paciente no banco PEP
        db = Database()

        patient = db.get_patient(event["patient_id"])

        if patient is None:
            raise Exception(
                f"Paciente {event['patient_id']} não encontrado."
            )

        # Converte o paciente para um recurso FHIR
        patient_resource = map_patient(patient)

        print(f"\nPatient FHIR:\n{patient_resource}")

        # Envia o Patient para o servidor FHIR
        # patient_response = fhir.send_resource(patient_resource)
        patient_response = fhir.create_or_update_patient(patient_resource)

        print("\nPatient enviado ao servidor FHIR com sucesso.")
        print(patient_response)

        # Converte o evento clínico para um recurso FHIR
        resource = map_event_to_fhir(event)

        print(f"\nRecurso FHIR gerado:\n{resource}")

        # Envia o recurso para o servidor FHIR
        response = fhir.send_resource(resource)

        print("\nRecurso enviado ao servidor FHIR com sucesso.")
        print(response)

        # Confirma o processamento da mensagem
        ch.basic_ack(
            delivery_tag=method.delivery_tag
        )

    except Exception as e:

        print(f"\nErro ao processar mensagem: {e}")

        # Rejeita a mensagem (sem reenfileirar)
        ch.basic_nack(
            delivery_tag=method.delivery_tag,
            requeue=False
        )


# Retry
def create_connection():
    """
    Tenta conectar ao RabbitMQ até que o serviço esteja disponível.
    """

    while True:

        try:

            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=RABBITMQ_HOST
                )
            )

            print("Conectado ao RabbitMQ.")

            return connection

        except pika.exceptions.AMQPConnectionError:

            print(
                "RabbitMQ ainda não disponível. Tentando novamente em 5 segundos..."
            )

            time.sleep(5)


def start_consumer():
    """
    Inicializa o consumidor RabbitMQ.
    """

    connection = create_connection()

    channel = connection.channel()

    channel.queue_declare(
        queue=QUEUE_NAME,
        durable=True
    )

    channel.basic_qos(
        prefetch_count=1
    )

    channel.basic_consume(
        queue=QUEUE_NAME,
        on_message_callback=callback
    )

    print(f"\nAguardando mensagens da fila '{QUEUE_NAME}'...")

    channel.start_consuming()


if __name__ == "__main__":
    start_consumer()