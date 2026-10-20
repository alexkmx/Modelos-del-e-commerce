# Imagen base oficial de Python
FROM python:3.11-slim

# Evita que Python escriba archivos .pyc y fuerza la salida directa a la consola
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /code

# Copiar e instalar dependencias
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar el proyecto
COPY . /code/