from ..models import transacao_model
from api import db

def cadastrar_transacao(transacao):
    transacao_bd = transacao_model.Transacao(nome=transacao.nome, descricao=transacao.descricao,
                                    valor=transacao.valor, tipo=transacao.tipo)
    db.session.add(transacao_bd)
    db.session.commit()
    return transacao_bd

def listar_transacoes():
    transacoes = transacao_model.Transacao.query.all()
    return transacoes

def listar_transacao_id(id):
    transacao = transacao_model.Transacao.query.filter_by(id=id).first()
    return transacao

def editar_transacao(transacao_bd, transacao_nova):
    transacao_bd.nome = transacao_nova.nome
    transacao_bd.descricao = transacao_nova.descricao
    transacao_bd.valor = transacao_nova.valor
    transacao_bd.tipo = transacao_nova.tipo
    db.session.commit()
    return transacao_bd

def remover_transacao(transacao):
    db.session.delete(transacao)
    db.session.commit()