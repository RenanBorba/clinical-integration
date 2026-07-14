# Mapeamento HL7 FHIR
def map_event_to_fhir(event: dict):

    return {
        "resourceType": "Observation",
        "status": "final",
        "code": {
            "text": event["event_type"]
        },
        "subject": {
            "reference": f"Patient/{event['patient_id']}"
        },
        "effectiveDateTime": event["date"],
        "note": [
            {
                "text": event["description"]
            }
        ]
    }