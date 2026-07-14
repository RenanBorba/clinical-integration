def map_condition(event):

    return {
        "resourceType": "Condition",
        "clinicalStatus": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                    "code": "active"
                }
            ]
        },
        "subject": {
            # "reference": f"Patient/{event['patient_id']}"
            "reference": f"Patient/patient-{event['patient_id']}"
        },
        "recordedDate": event["date"],
        "note": [
            {
                "text": event["description"]
            }
        ]
    }