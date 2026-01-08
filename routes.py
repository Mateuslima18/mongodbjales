from flask import request, jsonify
from models import LivroModel
from pymongo.errors import ConfigurationError

def init_routes(app):
    @app.route('/', methods=['GET'])
    def home():
        return jsonify({
            'message': 'Bem-vindo à API da Livraria',
            'rotas': {
                'GET /livros': 'Listar livros com filtros e paginação',
                'GET /livros/<id>': 'Buscar livro por ID',
                'GET /categorias': 'Listar categorias',
                'GET /tags': 'Listar tags'
            }
        })

    @app.route('/livros', methods=['GET'])
    def get_livros():
        try:
            filtros = request.args.get('categoria')
            pagina = int(request.args.get('pagina', 1))
            por_pagina = int(request.args.get('por_pagina', 10))
            filtros_dict = {}
            if filtros:
                filtros_dict['categoria'] = filtros
            livros = LivroModel.buscar_livros(filtros_dict, pagina, por_pagina)
            return jsonify(livros)
        except ConfigurationError as e:
            return jsonify({'error': 'Erro de configuração do banco de dados', 'details': str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'Erro interno', 'details': str(e)}), 500

    @app.route('/livros/<livro_id>', methods=['GET'])
    def get_livro(livro_id):
        try:
            livro = LivroModel.buscar_livro_por_id(livro_id)
            if livro:
                return jsonify(livro)
            return jsonify({'error': 'Livro não encontrado'}), 404
        except ConfigurationError as e:
            return jsonify({'error': 'Erro de configuração do banco de dados', 'details': str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'Erro interno', 'details': str(e)}), 500

    @app.route('/categorias', methods=['GET'])
    def get_categorias():
        try:
            categorias = LivroModel.obter_categorias()
            return jsonify(categorias)
        except ConfigurationError as e:
            return jsonify({'error': 'Erro de configuração do banco de dados', 'details': str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'Erro interno', 'details': str(e)}), 500

    @app.route('/tags', methods=['GET'])
    def get_tags():
        try:
            tags = LivroModel.obter_tags()
            return jsonify(tags)
        except ConfigurationError as e:
            return jsonify({'error': 'Erro de configuração do banco de dados', 'details': str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'Erro interno', 'details': str(e)}), 500