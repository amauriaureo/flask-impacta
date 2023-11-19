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
def frutas(nome_fruta):
    if nome_fruta in cores_frutas:
        return cores_frutas[nome_fruta]
    return "Não sei"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8765)
