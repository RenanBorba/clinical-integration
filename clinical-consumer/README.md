# Clinical Consumer - HL7 FHIR R4

O objetivo foi simular um cenário real de interoperabilidade entre um sistema de Prontuário Eletrônico do Paciente (PEP) e uma plataforma FHIR, permitindo que eventos clínicos fossem processados de forma assíncrona e convertidos em recursos padronizados para compartilhamento de informações em saúde.

A solução foi desenvolvida em Python com FastAPI e utiliza um Consumer RabbitMQ responsável por consumir os eventos publicados na fila, buscar os dados necessários no banco de dados, realizar o mapeamento para recursos HL7 FHIR R4 e enviá-los para um servidor HAPI FHIR, garantindo a padronização e interoperabilidade das informações clínicas.

Durante o desenvolvimento foram implementados recursos FHIR como Patient, Practitioner, Observation e MedicationRequest, além de uma estratégia de sincronização idempotente utilizando requisições HTTP PUT para evitar registros duplicados.

Esse projeto permitiu aprofundar conhecimentos em:

## 🔹 Tecnologias utilizadas:
Python + FastAPI         

RabbitMQ para mensageria assíncrona     

Docker / Docker Compose    

HAPI FHIR Server (FHIR R4)             

PostgreSQL     

REST APIs                  

JSON / FHIR Resources

## 🔹 Recursos FHIR implementados:
✅ Patient Representação do cadastro do paciente com identificadores como CPF e CNS/SUS.

✅ Observation Registro de informações clínicas e observações.

✅ MedicationRequest Representação de prescrições e solicitações de medicamentos.

## 🔹 Fluxo desenvolvido:
Sistema clínico → API REST → RabbitMQ → Consumer → Mapper FHIR → HAPI FHIR Server

O projeto também contempla conceitos importantes de interoperabilidade:

✔ Comunicação assíncrona baseada em eventos    

✔ Idempotência utilizando PUT no FHIR         

✔ Referenciamento entre recursos FHIR (Patient, Practitioner, Observation etc.)   

✔ Containerização para facilitar implantação     

✔ Separação entre produtor e consumidor de eventos

<br>

Esse projeto reforçou na prática como padrões como HL7 FHIR podem ser aplicados para conectar diferentes sistemas de saúde, permitindo maior integração, rastreabilidade e troca segura de informações clínicas.

---

# Arquitetura da Solução

```text
Sistema Hospitalar (PEP)
        |
        |
        v
   REST API - FastAPI
        |
        |
        v
     RabbitMQ
        |
        |
        v
 Clinical Consumer
        |
        |
        v
    FHIR Mapper
        |
        |
        v
 HAPI FHIR Server (FHIR R4)
```

---

# Tecnologias Utilizadas

* Python 3.12
* FastAPI
* RabbitMQ
* Docker / Docker Compose
* PostgreSQL
* HAPI FHIR Server
* HL7 FHIR R4
* REST API
* JSON

---

# Objetivo do Projeto

Demonstrar uma solução de interoperabilidade em saúde capaz de integrar informações clínicas utilizando padrões abertos.

O projeto simula cenários encontrados em ambientes hospitalares, como:

* Integração entre sistemas PEP;
* Processamento de eventos clínicos;
* Comunicação assíncrona entre serviços;
* Padronização de dados utilizando HL7 FHIR;
* Persistência e consulta de recursos clínicos.

---

# Fluxo de Processamento

1. O sistema clínico envia um evento através da API REST.

2. A API valida os dados recebidos.

3. O evento é publicado em uma fila RabbitMQ.

4. O consumidor processa a mensagem de forma assíncrona.

5. Os dados são convertidos em recursos HL7 FHIR.

6. Os recursos são enviados ao servidor HAPI FHIR.

---

# Eventos Clínicos Implementados

## Medical Evolution

Representa uma evolução clínica recebida de um sistema hospitalar.

Exemplo de evento:

```json
{
  "event_type": "medical_evolution",
  "patient_id": 1,
  "professional_id": 101,
  "date": "2026-07-14T13:00:00",
  "description": "Paciente apresenta melhora clínica.",
  "observations": "Sem intercorrências."
}
```

Mapeamento realizado:

```
medical_evolution
        |
        v
Observation
```

---

## Prescription

Representa uma prescrição médica.

Exemplo:

```json
{
  "event_type": "prescription",
  "patient_id": 1,
  "professional_id": 101,
  "medication": "Dipirona",
  "date": "2026-07-13T18:20:00"
}
```

Mapeamento realizado:

```
prescription
        |
        v
MedicationRequest
```

---

# Recursos FHIR Implementados

## Patient

Representação do paciente.

Exemplo:

```json
{
  "resourceType": "Patient",
  "id": "patient-1",
  "identifier": [
    {
      "system": "urn:cpf",
      "value": "123.456.789-01"
    },
    {
      "system": "urn:sus",
      "value": "898001160123456"
    }
  ],
  "active": true,
  "name": [
    {
      "text": "João Carlos da Silva"
    }
  ],
  "gender": "male",
  "birthDate": "1985-03-15"
}
```

---

## Observation

Utilizado para representar informações clínicas recebidas como eventos de evolução ou observações.

Exemplo:

```json
{
  "resourceType": "Observation",

  "status": "final",

  "subject": {
    "reference": "Patient/patient-1"
  },

  "performer": [
    {
      "reference": "Practitioner/101"
    }
  ],

  "effectiveDateTime": "2026-07-14T13:00:00",

  "valueString": "Paciente apresenta melhora clínica."
}
```

Relacionamento:

```
Observation
      |
      |
      +---- Patient/patient-1

```

---

## MedicationRequest

Representa uma prescrição médica vinculada ao paciente.

Exemplo:

```json
{
  "resourceType": "MedicationRequest",

  "id": "1001",

  "status": "active",

  "intent": "order",

  "medicationCodeableConcept": {
    "text": "Dipirona"
  },

  "subject": {
    "reference": "Patient/patient-1"
  },

  "authoredOn": "2026-07-13T18:20:00"
}
```

Relacionamento:

```
MedicationRequest/1001
          |
          |
          +---- Patient/patient-1
```

---

# Estratégia de Identificação FHIR

Foi utilizado um identificador lógico para manter rastreabilidade entre o sistema de origem e o servidor FHIR.

Exemplo:

Sistema origem:

```
patient_id = 1
```

Recurso FHIR:

```
Patient/patient-1
```

Essa estratégia permite sincronização utilizando HTTP PUT:

```
PUT /Patient/patient-1
```

Garantindo comportamento idempotente:

* Criar caso o recurso não exista;
* Atualizar caso já exista;
* Evitar duplicidade de registros.

---

# Infraestrutura Docker

Serviços executados:

| Serviço             | Porta |
| ------------------- | ----- |
| FastAPI             | 8000  |
| RabbitMQ            | 5672  |
| RabbitMQ Management | 15672 |
| HAPI FHIR           | 8080  |
| PostgreSQL          | 5432  |

Executar:

```bash
docker compose up --build
```

---

# Em execução

<img width="1491" height="999" alt="Image" src="https://github.com/user-attachments/assets/e32b21d9-2d4c-4f77-a094-3ee321e6b94f" />

<img width="1487" height="996" alt="Image" src="https://github.com/user-attachments/assets/20d917e8-e395-4fb0-9cfd-6c05438f7abe" />

<img width="1497" height="992" alt="Image" src="https://github.com/user-attachments/assets/ddb9cccb-dcef-49d6-ad4e-d50acb6abcf9" />

<img width="1920" height="1041" alt="Image" src="https://github.com/user-attachments/assets/be6b7a0c-989f-4766-8b21-8464dd189941" />

<img width="1920" height="1039" alt="Image" src="https://github.com/user-attachments/assets/bed8f006-16d1-47a9-bdb4-8b758d12a0a2" />

---

# Conceitos Aplicados

✔ Arquitetura orientada a eventos <br>
✔ Comunicação assíncrona com RabbitMQ <br>
✔ APIs REST <br>
✔ HL7 FHIR R4 <br>
✔ Interoperabilidade em saúde <br>
✔ Mapeamento de dados clínicos <br>
✔ Dockerização <br>
✔ Integração entre sistemas hospitalares <br>
✔ Sincronização idempotente via PUT <br>

---

# Próximos Passos

* Implementação de Encounter para representar atendimentos;
* Melhorar modelagem de prescrições utilizando códigos padronizados;
* Validação dos recursos utilizando FHIR Validator;
* Implementação de autenticação OAuth2/JWT;
* Auditoria e rastreabilidade dos eventos;
* Criação de testes automatizados;
* Integração com cenários LIS/PEP.

---
