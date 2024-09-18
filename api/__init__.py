#Importação das dependências
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Criação da aplicação flask
app = Flask (__name__)
app.config.from_object('config')
#Instanciando o banco de dados na aplicação
db = SQLAlchemy(app)
mi = Migrate(app, db)

from .models import conta_model