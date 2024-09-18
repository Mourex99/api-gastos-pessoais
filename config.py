DEBUG = True

#Configuração do banco de dados
USERNAME = 'root'
PASSWORD = 'root'
SERVER = 'localhost'
DB = 'gerenciamento_flask'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "chave_moura"