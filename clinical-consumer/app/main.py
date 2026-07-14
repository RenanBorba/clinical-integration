from app.consumer import start_consumer

def main():
    """
    Inicializa o Consumer responsável por consumir
    mensagens da fila RabbitMQ e enviá-las ao servidor HL7 FHIR.
    """
    print("Iniciando Clinical Consumer...")

    start_consumer()


if __name__ == "__main__":
    main()