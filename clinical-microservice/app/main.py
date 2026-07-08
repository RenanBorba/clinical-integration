from fastapi import FastAPI
from app.routes import router

# Declara a API
app = FastAPI(
    title="Clinical Integration Microservice",
    description="Microserviço responsável por receber dados clínicos e publicar na fila RabbitMQ.",
    version="1.0.0"
)

# Decorator para rota
@app.get("/")
# Quando acessar a rota raíz irá executar a função
def root():

    return {
        "service": "Clinical Integration Microservice",
        "status": "running"
    }

# Quando acessar a rota /health irá executar a função
@app.get("/health")
def health():

    return {
        "status": "UP"
    }

# Junta rotas que foram definidas dentro do aplicativo principal (app)
app.include_router(router)