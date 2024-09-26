from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

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
    data = db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(5), nullable=False)
    protocolo = db.Column(db.String(50), nullable=False)
    atendimento = db.Column(db.String(200), nullable=False)
    natureza = db.Column(db.String(100), nullable=False)
    tempo_atendimento = db.Column(db.String(50), nullable=False)

# Criação do banco de dados
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    # Coleta os dados do formulário
    atendimento = Atendimento(
        codigo_cliente=request.form['codigo_cliente'],
        nome_cliente=request.form['nome_cliente'],
        data=request.form['data'.replace('-', '')],
        hora=request.form['hora'.replace('-', '')],
        protocolo=request.form['protocolo'],
        atendimento=request.form['atendimento'],
        natureza=request.form['natureza'],
        tempo_atendimento=request.form['tempo_atendimento']
    )
    
    # Adiciona o atendimento ao banco de dados
    db.session.add(atendimento)
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
