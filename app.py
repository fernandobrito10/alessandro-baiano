import pandas as pd
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
import csv

load_dotenv()

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# app.secret_key = os.getenv('SECRET_KEY')  # Adicione uma chave secreta no .env

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redireciona para a página de login se não autenticado

# Modelo para o usuário
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    atendimentos = db.relationship('Atendimento', backref='usuario', lazy=True)

# Modelo para o atendimento
class Atendimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_cliente = db.Column(db.String(50), nullable=False)
    nome_cliente = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(8), nullable=False)  # DDMMYYYY
    hora = db.Column(db.String(6), nullable=False)  # HHMMSS
    protocolo = db.Column(db.String(50), nullable=False)
    atendimento = db.Column(db.String(200), nullable=False)
    natureza = db.Column(db.String(100), nullable=False)
    tempo_atendimento = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Chave estrangeira

# Criação do banco de dados
with app.app_context():
    db.create_all()

# Função para carregar as naturezas do arquivo CSV
def carregar_naturezas():
    naturezas = []
    with open('naturezasnova1.csv', mode='r', encoding='ISO-8859-1') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            if 'natureza' in linha:
                naturezas.append(linha['natureza'])
    return naturezas

# Função para carregar o usuário a partir do ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rota para a página principal
@app.route('/')
def index():
    naturezas = carregar_naturezas()
    return render_template('index.html', naturezas=naturezas)

# Rota para registrar atendimento (apenas usuários autenticados)
@app.route('/registrar', methods=['POST'])
@login_required  # Apenas usuários logados podem registrar atendimentos
def registrar():
    codigo_cliente = request.form['codigo_cliente']
    nome_cliente = request.form['nome_cliente']

    # Processa a data para o formato DDMMYYYY
    data_original = request.form['data']  # Formato: YYYY-MM-DD
    ano, mes, dia = data_original.split('-')  # Divide a data
    data = f"{dia}{mes}{ano}"  # Formato DDMMYYYY

    # Processa a hora para o formato HHMMSS
    hora = request.form['hora'].replace(':', '')  # Formato HHMM

    protocolo = request.form['protocolo']
    atendimento = request.form['atendimento']
    natureza = request.form['natureza']
    tempo_atendimento = request.form['tempo_atendimento']

    novo_atendimento = Atendimento(
        codigo_cliente=codigo_cliente,
        nome_cliente=nome_cliente,
        data=data,
        hora=hora,
        protocolo=protocolo,
        atendimento=atendimento,
        natureza=natureza,
        tempo_atendimento=tempo_atendimento,
        user_id=current_user.id  # Associa o atendimento ao usuário logado
    )

    db.session.add(novo_atendimento)
    db.session.commit()

    return redirect('/atendimentos')


# Rota para visualizar os atendimentos
@app.route('/atendimentos')
@login_required  # Apenas usuários logados podem ver atendimentos
def ver_atendimentos():
    # Exibe apenas os atendimentos do usuário logado
    atendimentos = Atendimento.query.filter_by(user_id=current_user.id).all()
    return render_template('atendimentos.html', atendimentos=atendimentos)


# Rota para concluir (excluir) um atendimento
@app.route('/concluir/<int:id>')
@login_required
def concluir_atendimento(id):
    atendimento = Atendimento.query.get(id)
    if atendimento:
        db.session.delete(atendimento)
        db.session.commit()
    return redirect('/atendimentos')

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('index'))  # Redireciona para a página inicial após login
        else:
            flash('Nome de usuário ou senha incorretos.', 'error')
    
    return render_template('login.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        novo_usuario = User(username=username, password_hash=hashed_password)
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for('login'))  # Redireciona após o cadastro
    return render_template('cadastrar.html')

# Rota de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sessão', 'success')
    return redirect(url_for('login'))

# Criar usuário (apenas para fins de exemplo, remover em produção)
@app.route('/criar_usuario')
def criar_usuario():
    hashed_password = generate_password_hash('senha123', method='sha256')
    novo_usuario = User(username='admin', password_hash=hashed_password)
    db.session.add(novo_usuario)
    db.session.commit()
    return 'Usuário criado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
