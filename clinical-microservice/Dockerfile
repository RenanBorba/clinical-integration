FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

# Instala todas dependências de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
# Uvicorn executa app/main.py e coloca a API no ar
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]