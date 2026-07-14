def map_patient(patient):

    gender = {
        "Masculino": "male",
        "Feminino": "female"
    }

    return {

        "resourceType": "Patient",

        # "id": str(patient["patient_id"]),

        # patient_id mapeado para ex.: patient-1 
        # devido HAPI FHIR não aceitar ex.: Patient/1
        "id": f"patient-{patient['patient_id']}",

        "identifier": [
            {
                "system": "urn:cpf",
                "value": patient["cpf"]
            },
            {
                "system": "urn:sus",
                "value": patient["sus"]
            }
        ],

        "active": True,

        "name": [
            {
                "text": patient["full_name"]
            }
        ],

        "gender": gender.get(patient["gender"], "unknown"),

        "birthDate": str(patient["birth_date"])
    }