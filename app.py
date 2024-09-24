from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista que armazena os atendimentos
atendimentos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    # Coleta os dados do formulário
    atendimento = {
        'codigo_cliente': request.form['codigo_cliente'],
        'nome_cliente': request.form['nome_cliente'],
        'data': request.form['data'],
        'hora': request.form['hora'],
        'protocolo': request.form['protocolo'],
        'atendimento': request.form['atendimento'],
        'natureza': request.form['natureza'],
        'tempo_atendimento': request.form['tempo_atendimento']
    }
    
    # Adiciona o atendimento à lista
    atendimentos.append(atendimento)
    
    # Redireciona para a página de atendimentos
    return redirect('/atendimentos')

@app.route('/atendimentos')
def ver_atendimentos():
    # Exibe os atendimentos registrados
    return render_template('atendimentos.html', atendimentos=atendimentos)

@app.route('/concluir/<int:index>')
def concluir_atendimento(index):
    # Remove o atendimento da lista
    if 0 <= index < len(atendimentos):
        atendimentos.pop(index)
    
    # Redireciona para a página de atendimentos
    return redirect('/atendimentos')

if __name__ == '__main__':
    app.run(debug=True)
