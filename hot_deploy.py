from flask import Flask
app = Flask(__name__)


@app.route("/")
def bom_dia():
    return "Bom dia"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8765, debug=True)
