def map_medication_request(event):

    return {
        "resourceType": "MedicationRequest",
        "status": "active",
        "intent": "order",
        "subject": {
            # "reference": f"Patient/{event['patient_id']}"
            "reference": f"Patient/patient-{event['patient_id']}"
        },
        # "requester": {
            # "reference": f"Practitioner/{event['professional_id']}"
        # },
        "authoredOn": event["date"],
        "medicationCodeableConcept": {
            "text": event["description"]
        }
    }