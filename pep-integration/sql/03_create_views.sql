BEGIN;

CREATE VIEW vw_patients AS
SELECT
    patient_id, 
    medical_record_number, 
    national_health_id,
    cpf, 
    full_name, 
    social_name, 
    birth_date, 
    gender, 
    marital_status, 
    mother_name, 
    father_name, 
    phone,
    email, 
    address, 
    city, 
    state,
    zip_code, 
    blood_type, 
    rh_factor,
    deceased,
    created_at, 
    updated_at
FROM patients;

-- 1. Evoluções Médicas
CREATE VIEW vw_medical_evolution AS
SELECT
    evolution_id,
    patient_id,
    evolution_date,
    professional_id,
    evolution_description,
    vital_signs,
    clinical_status,
    observations
FROM medical_evolution;

-- 2. Anamneses
CREATE VIEW vw_anamnesis AS
SELECT
    anamnesis_id,
    patient_id,
    anamnesis_date,
    professional_id,
    clinical_history,
    chief_complaint,
    lifestyle,
    family_history,
    allergies
FROM anamnesis;

-- 3. Receituários
CREATE VIEW vw_prescription AS
SELECT
    prescription_id,
    patient_id,
    prescription_date,
    professional_id,
    medication,
    dosage,
    administration_frequency,
    treatment_duration,
    observations
FROM prescriptions;

COMMIT;