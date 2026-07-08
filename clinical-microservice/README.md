# Clinical Integration Microservice

Microserviço responsável por receber eventos clínicos via API REST, validar os dados recebidos e publicá-los em uma fila RabbitMQ para processamento assíncrono.

Este componente representa a camada de integração da plataforma, desacoplando o sistema de origem dos responsáveis pelo processamento dos eventos.

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

## Para Executar

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

## Em Execução

<img width="1269" height="989" alt="Image" src="https://github.com/user-attachments/assets/bf2c8c97-0c93-410a-87af-610b5a6c26b8" />
<img width="1920" height="685" alt="Image" src="https://github.com/user-attachments/assets/46646342-fd4c-4102-9e8b-aa5454d8fc5c" />
<img width="1919" height="684" alt="Image" src="https://github.com/user-attachments/assets/3b8809f1-a02c-4c67-b6ae-8a783e6808a0" />
<img width="1920" height="683" alt="Image" src="https://github.com/user-attachments/assets/82a8955a-feab-4c53-84db-f828ff6e5eb8" />
<img width="1920" height="683" alt="Image" src="https://github.com/user-attachments/assets/6dd3f1e2-51ce-4e16-9319-c9a6ffd5c725" />
<img width="1036" height="346" alt="Image" src="https://github.com/user-attachments/assets/cb21158f-1fdf-4229-b03d-6080102b570a" />
<img width="1036" height="379" alt="Image" src="https://github.com/user-attachments/assets/c2dde3f5-9e90-4131-881b-af67c222257f" />
<img width="1920" height="1039" alt="Image" src="https://github.com/user-attachments/assets/4ef4c699-c8ba-4fb5-a2db-7f544e86edc3" />
<img width="1920" height="1042" alt="Image" src="https://github.com/user-attachments/assets/e39ec0c4-4593-4d2d-b616-1b747a18b355" />
<img width="1920" height="1040" alt="Image" src="https://github.com/user-attachments/assets/f4cdcfb7-8fa4-4292-87b4-edc93a625075" />
<img width="1920" height="1039" alt="Image" src="https://github.com/user-attachments/assets/8ad6303c-ebfa-43c0-ad36-3ff603de2010" />
<img width="1920" height="1040" alt="Image" src="https://github.com/user-attachments/assets/25580e2d-50e7-4f3f-b836-63c9c447e93e" />
<img width="1920" height="1039" alt="Image" src="https://github.com/user-attachments/assets/065bd7a8-e104-4489-8fd4-86cad5009329" />
<img width="1920" height="1039" alt="Image" src="https://github.com/user-attachments/assets/55a10fdb-9a52-49fc-bd33-fba6d9807ffa" />
<img width="1920" height="1039" alt="Image" src="https://github.com/user-attachments/assets/6a997fc7-7eb5-4994-bbee-b1877dc9b53c" />
<img width="1920" height="1038" alt="Image" src="https://github.com/user-attachments/assets/4ef033f4-4789-4016-a1fa-69ee921768a5" />

<br><br>


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

Este microserviço faz parte do projeto **Clinical Integration Platform**, disponível na raiz do repositório.
