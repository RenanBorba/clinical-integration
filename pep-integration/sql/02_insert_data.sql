BEGIN;

INSERT INTO patients (
    medical_record_number, national_health_id, cpf, full_name, social_name, 
    birth_date, gender, marital_status, mother_name, father_name, phone, 
    email, address, city, state, zip_code, blood_type, rh_factor, deceased
)
VALUES
(
    'MRN000001', '898001160123456', '123.456.789-01', 'João Carlos da Silva', NULL, 
    '1985-03-15', 'Masculino', 'Casado', 'Maria Aparecida da Silva', 'José Carlos da Silva', 
    '(11) 98765-4321', 'joao.silva@email.com', 'Rua das Flores, 123', 'São Paulo', 'SP', 
    '01000-000', 'O', '+', FALSE
),
(
    'MRN000002', '898001160654321', '987.654.321-00', 'Ana Beatriz Oliveira', 'Ana B. Oliveira', 
    '1992-08-22', 'Feminino', 'Solteira', 'Patrícia Oliveira', 'Carlos Oliveira', 
    '(11) 99876-5432', 'ana.oliveira@email.com', 'Av. Paulista, 1500', 'São Paulo', 'SP', 
    '01310-200', 'A', '-', FALSE
);

-- 1. Evoluções Médicas
INSERT INTO medical_evolution (patient_id, evolution_date, professional_id, evolution_description, clinical_status)
VALUES (1, NOW(), 101, 'Paciente apresenta melhora clínica.', 'Estável');

UPDATE medical_evolution
SET vital_signs = '{
        "blood_pressure": "120x80",
        "heart_rate": 72,
        "temperature": 36.7,
        "oxygen_saturation": 98,
        "respiratory_rate": 16
    }', -- Removi o ::jsonb que estava anteriormente, salvando como TEXT
    observations = 'Paciente orientado a manter uso da medicação anti-hipertensiva, realizar controle domiciliar da pressão arterial e retornar para reavaliação em 7 dias.'
WHERE evolution_id = 1;

INSERT INTO medical_evolution (patient_id, evolution_date, professional_id, evolution_description, vital_signs, clinical_status, observations)
VALUES
(
    2, NOW(), 1, 
    'Paciente apresenta melhora da dor abdominal após início da terapêutica medicamentosa. Refere redução das náuseas e boa aceitação da dieta líquida.',
    '{
        "blood_pressure":"118x76",
        "heart_rate":74,
        "temperature":36.5,
        "oxygen_saturation":99,
        "respiratory_rate":16
    }', -- Removido o ::jsonb
    'Melhora',
    'Paciente orientada a manter hidratação adequada e retornar em caso de piora dos sintomas.'
);

-- 2. Anamneses
INSERT INTO anamnesis (patient_id, anamnesis_date, professional_id, clinical_history, chief_complaint, lifestyle, family_history, allergies)
VALUES
(
    1, NOW(), 1, 
    'Paciente com histórico de hipertensão arterial há 10 anos, em uso contínuo de losartana 50 mg. Nega diabetes e cirurgias prévias.',
    'Cefaleia persistente há 3 dias, acompanhada de tontura.',
    'Não fumante, consumo ocasional de álcool, pratica caminhada 3 vezes por semana.',
    'Pai hipertenso e mãe diabética.',
    'Alergia à dipirona.'
);

INSERT INTO anamnesis (patient_id, anamnesis_date, professional_id, clinical_history, chief_complaint, lifestyle, family_history, allergies)
VALUES
(
    2, NOW(), 1, 
    'Paciente sem doenças crônicas conhecidas. Nega uso contínuo de medicamentos.',
    'Dor abdominal e náuseas iniciadas há aproximadamente 12 horas.',
    'Sedentária, não fumante, não ingere bebidas alcoólicas.',
    'Sem histórico familiar relevante.',
    'Nenhuma alergia conhecida.'
);

-- 3. Receituários
INSERT INTO prescriptions (patient_id, prescription_date, professional_id, medication, dosage, administration_frequency, treatment_duration, observations)
VALUES
(
    1, NOW(), 1, 'Paracetamol 750 mg', '1 comprimido', 'A cada 6 horas', '5 dias', 
    'Administrar após as refeições. Retornar caso os sintomas persistam.'
);

INSERT INTO prescriptions (patient_id, prescription_date, professional_id, medication, dosage, administration_frequency, treatment_duration, observations)
VALUES
(
    2, NOW(), 1, 'Omeprazol 20 mg', '1 cápsula', 'Uma vez ao dia', '14 dias', 
    'Administrar em jejum pela manhã.'
);

COMMIT;