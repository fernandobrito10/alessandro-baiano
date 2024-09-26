import pandas as pd
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import csv

load_dotenv()

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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

@app.route('/')
def index():
    naturezas = carregar_naturezas()  # Carrega as naturezas
    return render_template('index.html', naturezas=naturezas)  # Passa as naturezas para o template

@app.route('/registrar', methods=['POST'])
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
        tempo_atendimento=tempo_atendimento
    )
    
    db.session.add(novo_atendimento)
    db.session.commit()
    
    # Redireciona para a página de atendimentos
    return redirect('/atendimentos')

@app.route('/atendimentos')
def ver_atendimentos():
    # Exibe os atendimentos registrados
    atendimentos = Atendimento.query.all()
    return render_template('atendimentos.html', atendimentos=atendimentos)

@app.route('/concluir/<int:id>')
def concluir_atendimento(id):
    # Remove o atendimento do banco de dados
    atendimento = Atendimento.query.get(id)
    if atendimento:
        db.session.delete(atendimento)
        db.session.commit()
    
    # Redireciona para a página de atendimentos
    return redirect('/atendimentos')

if __name__ == '__main__':
    app.run(debug=True)
