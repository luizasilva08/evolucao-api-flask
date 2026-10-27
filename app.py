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

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()

    book = Book(
        title=data["title"],
        author=data["author"],
        description=data["description"]
    )

    db.session.add(book)
    db.session.commit()

    return jsonify({
        "message": "Livro inserido com sucesso"
    }), 201

@app.route("/books", methods=["GET"])
def get_all_books():
    books = Book.query.all()

    return jsonify([
        book.as_dict()
        for book in books
    ])

@app.route("/books/<uuid:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)

    return jsonify(book.as_dict())

@app.route("/books/<uuid:book_id>", methods=["PATCH"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)

    data = request.get_json()

    for key, value in data.items():
        setattr(book, key, value)

    db.session.commit()

    return jsonify({
        "message": "Livro atualizado com sucesso"
    })

@app.route("/books/<uuid:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)

    db.session.delete(book)
    db.session.commit()

    return jsonify({
        "message": "Livro removido com sucesso"
    })

@app.get("/books/favorites")          #lista os livros que estão favoritados
def list_favorites():
    books = Book.query.filter_by(is_favorite=True).all()
    return jsonify([
        book.as_dict() 
        for book in books
        ]), 200

@app.get("/books/reading")           #lista os livros que estão em leitura
def list_reading():
    books = Book.query.filter_by(is_reading=True).all()
    return jsonify([
        book.as_dict() 
        for book in books
        ]), 200

@app.get("/books/finished")           #lista os livros que estão em leitura
def list_finished():
    books = Book.query.filter_by(is_finished=True).all()
    return jsonify([
        book.as_dict() 
        for book in books
        ]), 200

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )