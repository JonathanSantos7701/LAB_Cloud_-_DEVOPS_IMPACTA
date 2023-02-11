from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Que Bom que você chegou aqui ! "