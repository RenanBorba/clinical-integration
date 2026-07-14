import requests

from app.config import FHIR_SERVER_URL

class FHIRService:
    """
    Responsável pela comunicação com o servidor HL7 FHIR.
    """

    def __init__(self):
        self.base_url = FHIR_SERVER_URL.rstrip("/")

    def create_or_update_patient(self, patient: dict):
        """
        Cria ou atualiza um Patient no servidor FHIR.

        Utiliza o método PUT para garantir sincronização do recurso,
        evitando a criação de pacientes duplicados.
        """

        patient_id = patient["id"]

        response = requests.put(
            url=f"{self.base_url}/Patient/{patient_id}",
            json=patient,
            headers={
                "Content-Type": "application/fhir+json"
            },
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    def send_resource(self, resource: dict):
        """
        Envia um recurso FHIR (Observation, Condition,
        MedicationRequest, etc.) para o servidor.
        """

        resource_type = resource.get("resourceType")

        if not resource_type:
            raise ValueError(
                "O recurso FHIR deve possuir o campo 'resourceType'."
            )

        response = requests.post(
            url=f"{self.base_url}/{resource_type}",
            json=resource,
            headers={
                "Content-Type": "application/fhir+json"
            },
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    def get_resource(self, resource_type: str, resource_id: str):
        """
        Consulta um recurso FHIR pelo ID.
        """

        response = requests.get(
            url=f"{self.base_url}/{resource_type}/{resource_id}",
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    def update_resource(
        self,
        resource_type: str,
        resource_id: str,
        resource: dict
    ):
        """
        Atualiza um recurso FHIR existente.
        """

        response = requests.put(
            url=f"{self.base_url}/{resource_type}/{resource_id}",
            json=resource,
            headers={
                "Content-Type": "application/fhir+json"
            },
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    def delete_resource(
        self,
        resource_type: str,
        resource_id: str
    ):
        """
        Remove um recurso FHIR.
        """

        response = requests.delete(
            url=f"{self.base_url}/{resource_type}/{resource_id}",
            timeout=10
        )

        response.raise_for_status()

        return response.status_code