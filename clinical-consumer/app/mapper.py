from app.mappers.patient_mapper import map_patient
from app.mappers.observation_mapper import map_observation
from app.mappers.condition_mapper import map_condition
from app.mappers.medication_mapper import map_medication_request

def map_event_to_fhir(event):
    # Mapeamento conforme event_type
    event_type = event["event_type"]
    
    if event_type == "patient":
        return map_patient(event)

    if event_type == "medical_evolution":
        return map_observation(event)

    elif event_type == "anamnesis":
        return map_condition(event)

    elif event_type == "prescription":
        return map_medication_request(event)

    # Caso tipo de event_type esteja errado
    raise ValueError(f"Tipo de evento inválido: {event_type}")