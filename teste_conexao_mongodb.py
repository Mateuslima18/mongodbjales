import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.errors import ConfigurationError

load_dotenv()

mongo_uri = os.getenv('MONGO_URI')
if not mongo_uri:
    print("MONGO_URI não encontrada no .env")
    exit(1)

try:
    client = MongoClient(mongo_uri)
    # Testar conexão
    client.admin.command('ping')
    print("Conexão com MongoDB Atlas bem-sucedida!")
except ConfigurationError as e:
    print(f"Erro de configuração: {e}")
except Exception as e:
    print(f"Erro na conexão: {e}")