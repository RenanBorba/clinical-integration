# Clinical Integration Microservice

Microserviço responsável por receber eventos clínicos via API REST, validar os dados recebidos e publicá-los em uma fila RabbitMQ para processamento assíncrono.

Este componente representa a camada de integração da plataforma, desacoplando o sistema de origem dos consumidores responsáveis pelo processamento dos eventos.

---

## Responsabilidades

- Receber eventos clínicos via HTTP
- Validar o payload utilizando Pydantic
- Converter os dados para JSON
- Publicar mensagens na fila RabbitMQ
- Disponibilizar documentação automática da API (Swagger/OpenAPI)

---

## Arquitetura

```text
Cliente
    │
    ▼
POST /clinical-data
    │
    ▼
FastAPI
    │
    ▼
Validação (Pydantic)
    │
    ▼
Publisher
    │
    ▼
RabbitMQ
```

---

## Estrutura

```text
clinical-microservice/
│
├── app/
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   ├── publisher.py
│   └── routes.py
│
├── tests/
│   ├── test_api.py
│   └── test_validation.py
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Tecnologias

- Python 3.12
- FastAPI
- Pydantic
- RabbitMQ
- Docker
- PostgreSQL
- Pytest

---

## Endpoints

### GET /

Verifica se a API está em execução.

Resposta:

```json
{
  "service": "Clinical Integration Microservice",
  "status": "running"
}
```

---

### GET /health

Health Check da aplicação.

Resposta:

```json
{
  "status": "UP"
}
```

---

### POST /clinical-data

Recebe um evento clínico e o publica na fila RabbitMQ.

#### Exemplo de requisição

```json
{
  "event_type": "medical_evolution",
  "patient_id": 1,
  "professional_id": 101,
  "date": "2026-07-02T17:30:00",
  "description": "Paciente apresenta melhora clínica.",
  "observations": "Sem intercorrências."
}
```

#### Exemplo de resposta

```json
{
  "status": "success",
  "message": "Dados enviados para processamento."
}
```

---

## Executando

Na raiz do projeto:

```bash
docker compose up --build
```

---

## Documentação da API

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

## Testes

Executar todos os testes:

```bash
pytest -v
```

---

## Fluxo de Processamento

1. O cliente envia um evento clínico para a API.
2. O FastAPI recebe a requisição.
3. O Pydantic valida o payload.
4. O payload é convertido para JSON.
5. O Publisher envia a mensagem para a fila RabbitMQ.
6. O evento permanece na fila até ser consumido por outro serviço.

---

## Configuração

As configurações são realizadas por meio do arquivo `.env`.

Principais variáveis utilizadas:

| Variável | Descrição |
|----------|-----------|
| POSTGRES_HOST | Host do PostgreSQL |
| POSTGRES_PORT | Porta do PostgreSQL |
| POSTGRES_DB | Banco de dados |
| POSTGRES_USER | Usuário |
| POSTGRES_PASSWORD | Senha |
| RABBITMQ_HOST | Host do RabbitMQ |
| RABBITMQ_PORT | Porta do RabbitMQ |
| QUEUE_NAME | Nome da fila |

---

## Próximas Evoluções

- Consumer RabbitMQ
- Persistência dos eventos
- Dead Letter Queue (DLQ)
- Retry automático
- Logs estruturados
- Observabilidade (Health Checks e métricas)
- Exchanges e Routing Keys para múltiplos tipos de eventos

---

Este microserviço faz parte do projeto **Clinical Integration Platform – LevelAI Case**, disponível na raiz do repositório.