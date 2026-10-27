#CONTEM OS MODELOS QUE REPRESENTAM AS ENTIDADES DO BANCO
#BOOK REPRESENTA A ENTIDADE BOOK
from uuid import uuid4

from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import UUID

from db import db 

class Book(db.Model):
#indicar que book é um modelo gerenciado pelo sqlalchemy
    __tablename__ = "book"
    #define o nome da tabela

    #ID
    id = db.Column(
        UUID(as_uuid=True), #vou usar o UUID
        primary_key = True, #chave primaria
        default = uuid4 #quando criar um novo livro, um UUID será criado
    )

    #TITULO
    title = db.Column(
        String (255), #recebe a string
        nullable = False #não aceita nulo
    )

    #AUTOR
    author = db.Column(
        String(255),
        nullable = False 
    )

    #title e author são obrigatórios

    #DESCRIÇÃO
    description = db.Column(
        Text, #textos maiores
        nullable = False
    )

    #FAVORITAR
    is_favorite = db.Column (
        db.Boolean,
        nullable = False,
        default = False
    )

    #LENDO
    is_reading = db.Column(
        db.Boolean,
        nullable = False,
        default = False
    )

    #FINALIZADO
    is_finished = db.Column(
        db.Boolean,
        nullable = False,
        default = False
    )

    published_year = db.Column(
    db.Integer,
    nullable=True
    )

#Transformando o modelo em dicionário, é o que mostrado em json (GET)

    def as_dict(self):
        return{
            "id":str(self.id), #necessário conversão forçada
            "title":self.title,
            "author":self.author,
            "description":self.description,
            "is_favorite":self.is_favorite,
            "is_reading":self.is_reading,
            "is_finished":self.is_finished,
            "published_year":self.published_year
        }

"""
POR ISSO SERÁ CRIADO UM MÉTODO RESPONSÁVEL POR TRANSFORMAR
O OBJETO BOOK EM UM DICIONÁRIO PYTHON

QUANDO OCORRER UMA CONSULTAR AO NOSSO SISTEMA ELE RETORNA UM OBJETO BOOK,
ELE NÃO É SIMPLESMENTE UM DICT PYTHON. 
O MÉTODO AS_DICT() FUNCIONA COMO UMA CAMADA DE CONVERSÃO, SELECIONANDO
APENAS O NECESSÁRIO PARA SER EXPOSTO PELA API E TRANSFORMANDO EM UM DICT,
ESTRUTURA QUE PODE SER FACILMENTE SERIALIZADA PARA JSON NA RESPOSTA HTTP
"""


