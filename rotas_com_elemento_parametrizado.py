from flask import Flask
app = Flask(__name__)

cores_frutas = {
    "morango": "vermelho",
    "uva": "roxo",
    "banana": "amarelo",
    "abacaxi": "amarelo",
    "limao": "verde",
}

@app.route("/frutas/<nome_fruta>/cor")
