from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app import db,bcrypt
from app.models import usuario, turmas, atividades

class loginForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btnSubmit = SubmitField('Cadastrar')

    def login(self):
        # recuperar o usuario do email
        user = usuario.query.filter_by(email=self.email.data).first()
        # verificar se a senha é valida
        if user:
            if self.senha.data:
                # retorna o user
                return user
            else:
                raise Exception("Senha incorreta")
            
        else:
            raise Exception("Usuario nao encontrado")
        

class TurmaPost(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    btnSubmit = SubmitField('Cadastrar')

    def save(self, user_id):
        turma = turmas (
            nome_turma = self.nome.data,
            user_id = user_id
        )
        db.session.add(turma)
        db.session.commit()

class AtividadePost(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    btnSubmit = SubmitField('Cadastrar')

    def save(self, user_id, turma_id):
        atv = atividades (
            nome_atividade = self.nome.data,
            user_id = user_id,
            turma_id = turma_id
        )
        db.session.add(atv)
        db.session.commit()