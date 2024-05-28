from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return usuario.query.get(user_id)

class usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    senha = db.Column(db.String, nullable=True)
    posts = db.relationship('turmas',backref='usuario',lazy=True)

class turmas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_turma = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)

class atividades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_atividade = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=True)
