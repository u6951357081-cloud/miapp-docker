# Imagen base
FROM python:3.10-slim

# Crear carpeta de la app
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la app
COPY app.py .

# Exponer el puerto interno
EXPOSE 5000

# Comando de ejecución
CMD ["python", "app.py"]

