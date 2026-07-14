def map_observation(event):

    return {
        "resourceType": "Observation",
        "status": "final",
        "subject": {
            # "reference": f"Patient/{event['patient_id']}"
            "reference": f"Patient/patient-{event['patient_id']}"
        },
        # Como a tabela "Profissional" não foi criada no exemplo, 
        # referência com Practitioner está comentada
        # "performer": [
            # {
                # "reference": f"Practitioner/{event['professional_id']}"
            # }
        # ],
        "effectiveDateTime": event["date"],
        "valueString": event["description"]
    }