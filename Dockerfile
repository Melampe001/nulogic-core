FROM python:3.12-slim

WORKDIR /app

# Instalar dependencias del sistema operativo si es necesario
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar requerimientos de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente del proyecto
COPY . .

# Exponer el puerto predeterminado de Uvicorn/FastAPI
EXPOSE 8000

# Comando de ejecución por defecto para producción
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
