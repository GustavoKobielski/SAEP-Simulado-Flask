from app import app, db
from flask import render_template, url_for, request, redirect, session
from app.forms import loginForm, TurmaPost, AtividadePost
from app.models import usuario, turmas, atividades
from flask_login import login_user, current_user, logout_user

bb = 0

@app.route('/', methods=['GET', 'POST'])
def homepage():
    form = loginForm()
    
    turmass = turmas.query.all()

    if form.validate_on_submit():
        user = form.login()
        login_user(user,remember=True)
        
    return render_template('index.html', form=form, turmass=turmass)

@app.route('/sair/')
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/cadastrarTurma/', methods=['GET', 'POST'])
def cadastrarTurma():
    form = TurmaPost()
    if form.validate_on_submit():
        form.save(current_user.id)
        return redirect(url_for('homepage'))
    return render_template('cadastrarTurma.html', form=form)

@app.route('/excluir/<id>')
def excluirTurma(id):
    entry = turmas.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('homepage'))

@app.route('/visualizar/<id>')
def VisualizarTurma(id):
    turmass = turmas.query.get(id)
    session['bb'] = id
    postsComentarios = atividades.query.filter_by(turma_id=id).all()
    return render_template('visualizarTurma.html', turmass=turmass, postsComentarios=postsComentarios)

@app.route('/cadastrarAtividade/', methods=['GET', 'POST'])
def cadastrarAtividade():
    form = AtividadePost()
    if form.validate_on_submit():
        bb = session.get('bb')
        form.save(current_user.id, bb)
        return redirect(url_for('homepage'))
    return render_template('cadastrarAtividade.html', form=form)