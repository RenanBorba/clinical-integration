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
def test_root():
    # É como abrir o navegador e acessar http://localhost:8000/
    # Funciona como se fosse o Postman ou o Insomnia, 
    # também poderia ser executado client.post, client.put ou client.delete

    # O teste test_root() verifica se a API está disponível e,
    # se o endpoint raiz (GET /) responde corretamente com o código HTTP 200
    response = client.get("/")

    # Espera o código 200, caso retorne 404 o teste falhou
    assert response.status_code == 200

### Para executar: pytest -v ###