BEGIN;

CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY, -- SERIAL (Gera ID automático 1, 2, 3...)
    medical_record_number VARCHAR(20) UNIQUE NOT NULL, -- Nº Prontuário
    national_health_id VARCHAR(20), -- CNS
    cpf VARCHAR(14),
    full_name VARCHAR(200) NOT NULL,
    social_name VARCHAR(200),
    birth_date DATE NOT NULL,
    gender VARCHAR(20),
    marital_status VARCHAR(30),
    mother_name VARCHAR(200),
    father_name VARCHAR(200),
    phone VARCHAR(20),
    email VARCHAR(150),
    address VARCHAR(250),
    city VARCHAR(100),
    state VARCHAR(2),
    zip_code VARCHAR(10),
    blood_type VARCHAR(5),
    rh_factor CHAR(1),
    deceased BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 1. Evoluções Médicas
CREATE TABLE medical_evolution (
    evolution_id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL, -- Compatível com o SERIAL de pacientes
    evolution_date TIMESTAMP NOT NULL,
    professional_id INTEGER NOT NULL,
    evolution_description TEXT NOT NULL,
    vital_signs TEXT,
    clinical_status VARCHAR(50),
    observations TEXT,

    CONSTRAINT fk_patient
        FOREIGN KEY(patient_id)
        REFERENCES patients(patient_id)
);

-- 2. Anamneses
CREATE TABLE anamnesis (
    anamnesis_id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL, -- Compatível com o SERIAL de pacientes
    anamnesis_date TIMESTAMP,
    professional_id INTEGER,
    clinical_history TEXT,
    chief_complaint TEXT,
    lifestyle TEXT,
    family_history TEXT,
    allergies TEXT,

    FOREIGN KEY(patient_id)
        REFERENCES patients(patient_id)
);

-- 3. Receituários
CREATE TABLE prescriptions (
    prescription_id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL, -- Compatível com o SERIAL de pacientes
    prescription_date TIMESTAMP,
    professional_id INTEGER,
    medication VARCHAR(150),
    dosage VARCHAR(100),
    administration_frequency VARCHAR(100),
    treatment_duration VARCHAR(100),
    observations TEXT,

    FOREIGN KEY(patient_id)
        REFERENCES patients(patient_id)
);

COMMIT;