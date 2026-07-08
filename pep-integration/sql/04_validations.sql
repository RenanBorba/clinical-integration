-- Validação 1 – Chave Primária Duplicada
SELECT
    evolution_id,
    COUNT(*)
FROM vw_medical_evolution
GROUP BY evolution_id
HAVING COUNT(*) > 1;

-- Validação 2 – Campos Obrigatórios Nulos
SELECT *
FROM vw_medical_evolution
WHERE evolution_id IS NULL
   OR patient_id IS NULL
   OR professional_id IS NULL
   OR evolution_date IS NULL
   OR evolution_description IS NULL;

-- Validação 3 – Pacientes inexistentes
SELECT e.patient_id
FROM vw_medical_evolution e
LEFT JOIN patients p
ON e.patient_id = p.patient_id
WHERE p.patient_id IS NULL;

-- Validação 4 – Datas futuras
SELECT *
FROM vw_medical_evolution
WHERE evolution_date > CURRENT_TIMESTAMP;

-- Validação 5 – Receitas sem medicamento
SELECT *
FROM vw_prescription
WHERE medication IS NULL
   OR medication='';

-- Validação 6 – Dosagem inválida
SELECT *
FROM vw_prescription
WHERE dosage IS NULL;

-- Validação 7 – Anamnese sem histórico
SELECT *
FROM vw_anamnesis
WHERE clinical_history IS NULL;