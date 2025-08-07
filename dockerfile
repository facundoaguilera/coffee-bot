# Imagen base
FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements y archivos de configuración
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY src ./src

# Establecer PYTHONPATH para que reconozca app como paquete raíz
ENV PYTHONPATH=/app/src

# Copiar el .env si lo necesitás dentro del contenedor
#COPY .env .env

# Comando de inicio
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

