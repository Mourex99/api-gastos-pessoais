from api import db

class Conta(db.Model):
    __tablename__ = "conta"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    saldo = db.Column(db.Float, nullable=False)