from datetime import datetime
# Validação e serialização dos dados recebidos no POST
from pydantic import BaseModel

# Modelo (schema) do payload que a API espera receber
class ClinicalData(BaseModel):
# Mapeia o JSON recebido em um objeto Python
    event_type: str
    patient_id: int
    professional_id: int
    date: datetime
    description: str
    observations: str | None = None