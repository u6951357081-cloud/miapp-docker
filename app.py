from flask import Flask
import random

app = Flask(__name__)

frases = [
    "No cuentes los días, haz que los días cuenten.",
    "La mejor manera de predecir el futuro es creándolo.",
    "Cada error enseña una lección.",
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "Haz algo hoy que tu yo del futuro te agradezca."
]

@app.route("/")
def home():
    frase = random.choice(frases)
    return f"""
    <h1>🌟 Generador de Frases Motivadoras</h1>
    <p style='font-size:20px; color:#333;'>{frase}</p>
    <hr>
    <p>Aplicación web original desplegada en Docker.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

