from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/bom-dia")
@app.route("/good-morning")


def bom_dia():
    return "Bom dia"

@app.route("/boa-tarde")
@app.route("/good-afternoon")

def boa_tarde():
    return "Boa tarde"


@app.route("/boa-noite")
@app.route("/good-night")

def boa_noite():
    return "Boa noite"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8769)
