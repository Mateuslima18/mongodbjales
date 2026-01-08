import os
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
from bson.decimal128 import Decimal128

load_dotenv()

mongo_uri = os.getenv('MONGO_URI')

def get_db():
    client = MongoClient(mongo_uri)
    return client['livraria']

class LivroModel:
    @staticmethod
    def buscar_livros(filtros=None, pagina=1, por_pagina=10):
        # Implementar busca com filtros, paginação
        db = get_db()
        query = {}
        if filtros:
            if 'categoria' in filtros:
                query['categoria'] = filtros['categoria']
            if 'tags' in filtros:
                query['tags'] = {'$in': filtros['tags']}
            # Adicionar mais filtros se necessário

        skip = (pagina - 1) * por_pagina
        livros = list(db.livros.find(query).skip(skip).limit(por_pagina))
        return livros

    @staticmethod
    def buscar_livro_por_id(livro_id):
        # Implementar busca por ID
        db = get_db()
        try:
            livro = db.livros.find_one({'_id': ObjectId(livro_id)})
            return livro
        except:
            return None

    @staticmethod
    def obter_categorias():
        # Implementar obter categorias únicas
        db = get_db()
        categorias = db.livros.distinct('categoria')
        return categorias

    @staticmethod
    def obter_tags():
        # Implementar obter tags únicas
        db = get_db()
        tags = db.livros.distinct('tags')
        return tags

    # Adicionar outros métodos conforme necessário
    @staticmethod
    def buscar_livros(filtros=None, pagina=1, por_pagina=10):
        # Implementar busca com filtros, paginação
        query = {}
        if filtros:
            if 'categoria' in filtros:
                query['categoria'] = filtros['categoria']
            if 'tags' in filtros:
                query['tags'] = {'$in': filtros['tags']}
            # Adicionar mais filtros se necessário

        skip = (pagina - 1) * por_pagina
        livros = list(db.livros.find(query).skip(skip).limit(por_pagina))
        return livros

    @staticmethod
    def buscar_livro_por_id(livro_id):
        # Implementar busca por ID
        try:
            livro = db.livros.find_one({'_id': ObjectId(livro_id)})
            return livro
        except:
            return None

    @staticmethod
    def obter_categorias():
        # Implementar obter categorias únicas
        categorias = db.livros.distinct('categoria')
        return categorias

    @staticmethod
    def obter_tags():
        # Implementar obter tags únicas
        tags = db.livros.distinct('tags')
        return tags

    # Adicionar outros métodos conforme necessário