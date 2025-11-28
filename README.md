# Mi Aplicación Web con Flask y Docker

Esta es una aplicación web sencilla desarrollada en **Python** usando **Flask**. 
Muestra una frase motivadora aleatoria cada vez que se accede a la página.

Es parte de la Unidad 2 — Práctica 3: *Despliegue de aplicaciones web mediante virtualización y contenedores*.

---

##  Cómo ejecutar la aplicación en local

### 1. Instalar dependencias (solo si NO usas Docker)
pip install -r requirements.txt

### 2. Ejecutar la app
python app.py

La aplicación estará disponible en:

> http://localhost:5000

---

## Cómo construir y ejecutar el contenedor Docker

### 1. Construir la imagen
docker build -t miapp .

### 2. Ejecutar la imagen
docker run -p 5000:5000 miapp

---

## Contenido del proyecto

- `app.py` → Código de la aplicación Flask 
- `requirements.txt` → Dependencias de Python 
- `Dockerfile` → Instrucciones para construir la imagen Docker 
- `README.md` → Documentación del proyecto 

---

##  Funcionalidad de la aplicación

Cada vez que se accede a la página principal, se muestra una **frase motivadora aleatoria**, generada desde un pequeño listado definido en `app.py`.

---

## Autor

*MJC* 

