# Cria um cliente HTTP "falso" 
# que faz requisições diretamente para sua aplicação
from fastapi.testclient import TestClient
# O teste importa a aplicação (app) do main.py
from app.main import app

# Cria um cliente de testes
# Inicia a aplicação FastAPI em memória, consegue fazer requisições 
# para a API sem precisar executar o Uvicorn
client = TestClient(app)

# O nome começa com test_, então o Pytest reconhece automaticamente 
# essa função como um teste

# Validação automática do payload
def test_invalid_payload():

    # O teste faz a requisição enviando um JSON vazio.
    # Como todos os campos do schema são obrigatórios, quando chega vazio,
    # o FastAPI tenta criar ClinicalData(), porém como faltam todos os campos,
    # o próprio Pydantic gera um erro de validação 422 "unprocessable entity"
    response = client.post(
        "/clinical-data",
        json={}
    )

    assert response.status_code == 422

### Para executar: pytest -v ###