#Importação das dependências
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api

#Criação da aplicação flask
app = Flask (__name__)
app.config.from_object('config')
#Instanciando o banco de dados na aplicação
db = SQLAlchemy(app)
ma = Marshmallow(app)
mi = Migrate(app, db)

api = Api(app)
from .models import conta_model, transacao_model
from .views import conta_view, transacao_view