# PEP Integration (Database Layer)

## Objetivo

Este módulo representa a camada de integração do Prontuário Eletrônico do Paciente (PEP), disponibilizando informações clínicas por meio de **views SQL** para consumo por aplicações externas.

A utilização de views permite abstrair a estrutura física do banco de dados, promovendo desacoplamento, padronização dos dados e maior segurança nas integrações.

As views disponibilizam informações clínicas inspiradas em cenários encontrados em sistemas de gestão hospitalar, contemplando:

- Evoluções Médicas
- Anamneses
- Receituários

---

## Estrutura do Projeto

```
pep-integration/

├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_insert_data.sql
│   ├── 03_create_views.sql
│   └── 04_validations.sql
│
└── README.md
```

---

## Views Disponibilizadas

| View | Descrição |
|------|-----------|
| `vw_medical_evolution` | Disponibiliza as evoluções médicas dos pacientes. |
| `vw_anamnesis` | Disponibiliza os registros de anamneses. |
| `vw_prescription` | Disponibiliza os receituários médicos. |

Estas views representam a camada de integração que poderá ser consumida por sistemas externos sem acesso direto às tabelas transacionais.

---

## Arquitetura

```
Tabelas do PEP
       │
       ▼
Views SQL
       │
       ▼
Aplicações Externas
(FastAPI / Integrações / BI)
```

## Como Executar

Os scripts devem ser executados na ordem apresentada abaixo, pois possuem dependência entre si.

### 1. Criar as tabelas

```sql
SOURCE 01_create_tables.sql;
```

### 2. Inserir dados de exemplo

```sql
SOURCE 02_insert_data.sql;
```

### 3. Criar as Views

```sql
SOURCE 03_create_views.sql;
```

### 4. Executar as validações

```sql
SOURCE 04_validations.sql;
```

### PostgreSQL

Caso esteja utilizando o **psql**, execute:

```sql
\i 01_create_tables.sql
\i 02_insert_data.sql
\i 03_create_views.sql
\i 04_validations.sql
```

---

## Estrutura das Views

As views foram projetadas para disponibilizar somente as informações necessárias para integração, abstraindo a estrutura física das tabelas do banco.

### vw_medical_evolution

Contém informações referentes ao acompanhamento clínico do paciente.

Campos principais:

- ID da evolução
- ID do paciente
- Data da evolução
- Profissional responsável
- Descrição da evolução
- Sinais vitais
- Status clínico
- Observações

---

### vw_anamnesis

Disponibiliza o histórico clínico registrado durante o atendimento.

Campos principais:

- ID da anamnese
- ID do paciente
- Data da anamnese
- Profissional responsável
- Histórico clínico
- Queixa principal
- Hábitos de vida
- Histórico familiar
- Alergias

---

### vw_prescription

Disponibiliza as prescrições médicas.

Campos principais:

- ID da prescrição
- ID do paciente
- Data da prescrição
- Profissional responsável
- Medicamento
- Dosagem
- Frequência
- Duração do tratamento
- Observações

---

## Validações de Integridade

O script `04_validations.sql` contém consultas destinadas à validação da integridade dos dados disponibilizados pelas views.

As verificações incluem:

- ✔ Ausência de registros duplicados nas chaves primárias.
- ✔ Existência dos pacientes relacionados aos registros clínicos.
- ✔ Preenchimento dos campos obrigatórios.
- ✔ Datas válidas (não superiores à data atual).
- ✔ Existência de medicamentos cadastrados nas prescrições.
- ✔ Histórico clínico informado nas anamneses.
- ✔ Integridade referencial entre pacientes, evoluções, anamneses e receituários.

---

## Fluxo de Integração

1. Os dados clínicos são registrados nas tabelas do PEP.
2. As views consolidam e padronizam as informações.
3. Sistemas externos consultam exclusivamente as views.
4. As validações garantem a consistência dos dados disponibilizados.

## Benefícios da Utilização de Views

A utilização de views proporciona:

- Desacoplamento entre aplicações consumidoras e o banco transacional.
- Padronização dos dados disponibilizados.
- Maior segurança, evitando acesso direto às tabelas.
- Facilidade para evolução da estrutura física sem impacto nas integrações.

---

## Observação

As tabelas utilizadas neste projeto possuem finalidade exclusivamente acadêmica e simulam um cenário de integração entre um Prontuário Eletrônico do Paciente (PEP) e aplicações externas. A modelagem foi inspirada em cenários comuns de sistemas de gestão hospitalar utilizados no mercado de Saúde Digital, como Bionexo Tasy e MV Soul.