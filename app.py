#RESPONSAVEL PELA APLICACAO FLASK
#E PELOS ENDPOINTS
#APP DE GERENCIAMENTO DE LIVROS -
#CONSULTAR LIVROS
#EDITAR
#ATUALIZAR
#DELETAR
#FAVORITAR
#LIVROS EM LEITURA
#LIVROS FINALIZADOS

from flask import Flask
from db import db
from dotenv import load_dotenv
import os
from flask_migrate import Migrate
from models.book import Book
from flask import request, jsonify

load_dotenv() # Carrega o .env
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/hello", methods=["GET"])
def hello():
    return "API está funcionando!"

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )