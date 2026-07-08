from fastapi import APIRouter, HTTPException

from app.models import ClinicalData
from app.publisher import publish

# Declara o router
router = APIRouter()

# Declara a rota de post
@router.post(
    "/clinical-data",
    #202 accepted
    status_code=202,
    summary="Recebe informações clínicas",
    description="Valida os dados recebidos e publica a mensagem na fila RabbitMQ."
)
# Declara o endpoint e define que o payload da requisição deve seguir o schema ClinicalData (tipagem)
def receive_clinical_data(data: ClinicalData):
    # Tratamento de erros
    try:
        # Serializa esse objeto novamente em uma string JSON, 
        # que é o formato enviado no corpo da mensagem (body) para a fila
        publish(data.model_dump_json())

        return {
            "status": "accepted",
            "queue": "clinical_queue",
            "message": "Mensagem publicada com sucesso!"
    }

    # Armazena a exceção na variável "e"
    except Exception as e:

        raise HTTPException(
            # 503 service unavailable
            status_code=503,
            detail=f"Erro ao publicar mensagem: {str(e)}"
        )