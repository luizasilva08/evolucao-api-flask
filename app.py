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

load_dotenv() # Carrega o .env
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")