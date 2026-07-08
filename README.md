# Clinical Integration Platform

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-3.13-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED)

Projeto desenvolvido para simular uma arquitetura de integração entre um Prontuário Eletrônico do Paciente (PEP) e aplicações externas, utilizando tecnologias amplamente empregadas em ambientes hospitalares, como FastAPI, RabbitMQ, PostgreSQL e Docker.

O fluxo contempla a disponibilização de dados clínicos por meio de views SQL, o recebimento de eventos via API REST e sua publicação em uma fila RabbitMQ para processamento assíncrono.

O projeto foi inspirado em cenários de integração encontrados em soluções de Saúde Digital, como Philips Tasy e MV Soul.

---

## Arquitetura
```text
Sistema Hospitalar
        │
        ▼
 PostgreSQL (PEP)
        │
        ▼
   Views SQL
        │
        ▼
Clinical Integration API
      (FastAPI)
        │
        ▼
     RabbitMQ
```
---

## Estrutura do projeto

```
clinical-microservice/

├── clinical-microservice/
│   ├── app/
│   ├── tests/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
│
├── pep-integration/
│   ├── sql/
│   │   ├── 01_create_tables.sql
│   │   ├── 02_insert_data.sql
│   │   ├── 03_create_views.sql
│   │   └── 04_validations.sql
│   └── README.md
│
├── docker-compose.yml
├── .env
└── README.md
```

---

## Componentes

### PEP Integration

Responsável pela camada de dados do prontuário eletrônico.

Inclui:

- Modelagem das tabelas clínicas
- Dados de exemplo
- Views para integração
- Scripts de validação
- Garantia de integridade referencial

Mais detalhes:

📁 **pep-integration/README.md**

---

### Clinical Microservice

Microserviço responsável por:

- Receber eventos clínicos via REST
- Validar payload utilizando Pydantic
- Publicar mensagens na fila RabbitMQ
- Disponibilizar documentação Swagger
- Executar testes automatizados com Pytest

Mais detalhes:

📁 **clinical-microservice/README.md**

---

## Tecnologias

- Python 3.12
- FastAPI
- RabbitMQ
- PostgreSQL
- Docker
- Pydantic
- Pytest
- SQL

---

## Como executar

### Pré-requisitos

- Docker Desktop
- Docker Compose

---

### Executando

```bash
docker compose up --build
```

Após iniciar os containers:

API

http://localhost:8000

Swagger

http://localhost:8000/docs

Health Check

http://localhost:8000/health

RabbitMQ

http://localhost:15672

Usuário: guest

Senha: guest

<br>

#### Serviços

| Serviço | Endereço |
|----------|----------|
| API | http://localhost:8000 |
| Swagger | http://localhost:8000/docs |
| Health Check | http://localhost:8000/health |
| RabbitMQ | http://localhost:15672 |
| PostgreSQL | localhost:5432 |

---

## Fluxo da integração

1. O sistema envia um evento clínico para a API.
2. O FastAPI valida o payload utilizando Pydantic.
3. O payload validado é serializado em JSON.
4. A mensagem é publicada no RabbitMQ.
5. O RabbitMQ armazena a mensagem para processamento.
6. Um consumidor poderá processar a fila posteriormente.

---

## Exemplo de Payload

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

---

## Objetivos do projeto

Este projeto demonstra conhecimentos em:

- Arquitetura de Integração
- APIs REST
- Mensageria
- Modelagem de Banco de Dados
- Docker
- FastAPI
- RabbitMQ
- PostgreSQL
- Validação de dados
- Testes automatizados
- Boas práticas de organização de projetos

---

## Próximas evoluções

- Implementação de Consumer RabbitMQ
- Persistência de eventos processados
- Dead Letter Queue (DLQ)
- Logs estruturados
- Retry automático
- Observabilidade

---
