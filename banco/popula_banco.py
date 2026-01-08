import os
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.decimal128 import Decimal128
from pymongo.errors import ConfigurationError

load_dotenv()

mongo_uri = os.getenv('MONGO_URI')
try:
    client = MongoClient(mongo_uri)
    db = client['livraria']  # Nome do banco

    # Dados iniciais
    livros = [
        {
            "titulo": "O Senhor dos Anéis",
            "autor": "J.R.R. Tolkien",
            "preco": Decimal128("49.90"),
            "categoria": "Fantasia",
            "tags": ["aventura", "magia"],
            "data_publicacao": "1954-07-29"
        },
        {
            "titulo": "1984",
            "autor": "George Orwell",
            "preco": Decimal128("29.90"),
            "categoria": "Ficção Científica",
            "tags": ["distopia", "política"],
            "data_publicacao": "1949-06-08"
        },
        # Adicione mais livros conforme necessário
    ]

    # Inserir dados
    db.livros.insert_many(livros)
    print("Banco populado com sucesso!")
except ConfigurationError as e:
    print(f"Erro de configuração: {e}")
except Exception as e:
    print(f"Erro ao popular banco: {e}")