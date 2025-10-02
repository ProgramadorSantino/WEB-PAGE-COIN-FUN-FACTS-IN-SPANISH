from flask import Flask, url_for
import random

app = Flask(__name__)

# -----------------------------
# LISTA DE DATOS CURIOSOS
# -----------------------------
facts = [
    "🐝 Las abejas pueden reconocer rostros humanos.",
    "❤️ El corazón humano late alrededor de 100,000 veces al día.",
    "🐙 Los pulpos tienen tres corazones.",
    "🍯 La miel nunca caduca.",
    "🌍 El agua cubre más del 70% de la superficie de la Tierra.",
    "🧠 El cerebro humano tiene alrededor de 86 mil millones de neuronas.",
    "🔥 El Sol es 330,000 veces más masivo que la Tierra.",
    "🐧 Los pingüinos tienen una glándula que les permite beber agua salada.",
    "🎵 Las plantas pueden crecer más rápido si están expuestas a música.",
    "⚡ El rayo es cinco veces más caliente que la superficie del sol."
]

# -----------------------------
# PÁGINA PRINCIPAL
# -----------------------------
@app.route("/")
def home():
    # Esta página ofrece dos opciones:
    # 1. Ver un dato curioso
    # 2. Tirar una moneda
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Página de inicio</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: #e0f7fa;
            }}
            .container {{
                text-align: center;
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.2);
            }}
            a {{
                display: inline-block;
                margin: 10px;
                padding: 10px 20px;
                background-color: #007BFF;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                transition: background 0.3s;
            }}
            a:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>👋 Bienvenido</h1>
            <p>¿Qué quieres hacer?</p>
            <!-- Enlaces a las otras páginas -->
            <a href="{url_for('random_fact')}">✨ Aprender un dato curioso</a>
            <a href="{url_for('coin_flip')}">🪙 Tirar una moneda</a>
        </div>
    </body>
    </html>
    """

# -----------------------------
# PÁGINA DE DATOS CURIOSOS
# -----------------------------
@app.route("/curioso")
def random_fact():
    fact = random.choice(facts)  # Escoge un hecho aleatorio
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Dato Curioso</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #ffecd2, #fcb69f);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background-color: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 500px;
            }}
            h1 {{
                color: #333;
                margin-bottom: 15px;
            }}
            p {{
                font-size: 1.2em;
                color: #555;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #28a745;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                transition: background 0.3s;
            }}
            a:hover {{
                background-color: #1e7e34;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>✨ Dato Curioso ✨</h1>
            <p>{fact}</p>
            <!-- Botones de navegación -->
            <a href="{url_for('home')}">🏠 Volver al inicio</a>
            <a href="{url_for('random_fact')}">🔄 Ver otro dato</a>
        </div>
    </body>
    </html>
    """

# -----------------------------
# PÁGINA DE MONEDA
# -----------------------------
@app.route("/moneda")
def coin_flip():
    # Generamos un resultado aleatorio: "Cara" o "Cruz"
    result = random.choice(["🪙 Cara", "🪙 Cruz"])



    


    

    
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Tirar Moneda</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #c2e9fb, #a1c4fd);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background-color: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 400px;
            }}
            h1 {{
                color: #333;
                margin-bottom: 15px;
            }}
            p {{
                font-size: 1.5em;
                color: #555;
                font-weight: bold;
            }}
            a {{
                display: inline-block;
                margin: 10px;
                padding: 10px 20px;
                background-color: #ff9800;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                transition: background 0.3s;
            }}
            a:hover {{
                background-color: #e68900;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🪙 Lanzamiento de moneda</h1>
            <p>{result}</p>
            <!-- Botones de navegación -->
            <a href="{url_for('coin_flip')}">🔄 Volver a tirar</a>
            <a href="{url_for('home')}">🏠 Volver al inicio</a>
        </div>
    </body>
    </html>
    """

# -----------------------------
# EJECUCIÓN DEL SERVIDOR
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
