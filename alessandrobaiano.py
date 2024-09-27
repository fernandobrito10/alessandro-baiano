'''
Colar: X=80 Y=325, X=417 Y=323, X=669 Y=329
Novo atendimento: X=1320 Y=174
Pegar código do cliente: X=688 Y=219
Colocar código do cliente: X=34 Y=239
Negar coisas 1: X=723 Y=380
Negar coisas 2: X=681 Y=393
Pegar contato: X=688 Y=286
Colocar contato: X=429 Y=238
Pegar data: X=688 Y=354
Colocar data: X=549 Y=237
Pegar hora: X=688 Y=412
Colocar hora: X=624 Y=238
Escrever atendimento: X=49 Y=284
Colocar natureza: X=378 Y=282
Colocar tempo de atendimento: X=437 Y=395
Barra para rolar: X=1254 Y=203  
Ok para finalizar atendimento: X=1335 Y=175
'''
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2  # ou o adaptador que você estiver usando para o PostgreSQL
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from dotenv import load_dotenv
from flask_login import current_user
from monitoramento import monitorar_tela
import os
import time

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Atendimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def contar_atendimentos_por_usuario(user_id):
    return Atendimento.query.filter_by(user_id=user_id).count()

with app.app_context():
    total_atendimentos = contar_atendimentos_por_usuario(3)  # Substitua 1 pelo ID desejado
    print(f'Total de atendimentos do usuário: {total_atendimentos}')

if __name__ == '__main__':
    app.run()


time.sleep(2)

mouse = MouseController()
keyboard = KeyboardController()

def alttab():
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    time.sleep(0.1)
    keyboard.release(Key.alt)
    keyboard.release(Key.tab)
    time.sleep(0.5)

def clicaresquerdo():
    mouse.click(Button.left, 1)

def clicardireito():
    mouse.click(Button.right, 1)

def esc():
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

def tab():
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

time.sleep(1)

lista = ['Confirmação',
         'Informação']

# Novo atendimento
keyboard.press(Key.f2)
keyboard.release(Key.f2)

teste = monitorar_tela(lista)

if teste:
    print('Esc')
    esc()

teste = monitorar_tela(lista)

if teste:
    print('Esc')
    esc()

time.sleep(0.8)

tab()
time.sleep(0.2)
tab()
time.sleep(0.2)

alttab()

# Pegar código do cliente
mouse.position = (688, 219)
mouse.click(Button.left, 1)
time.sleep(1)
'''
# Novo atendimento
mouse.position = (1320, 174)
mouse.click(Button.left, 1)
time.sleep(1)

alttab()

# Pegar código do cliente
mouse.position = (688, 219)
mouse.click(Button.left, 1)
time.sleep(1)

alttab()

# Colocar código
mouse.position = (34, 239)
mouse.click(Button.left, 1)
mouse.click(Button.right, 1)
mouse.position = (91, 319)
mouse.click(Button.right, 1)
time.sleep(0.1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)

# Negar coisas
mouse.position = (723, 380)
mouse.click(Button.left, 1)
time.sleep(2)
mouse.position = (681, 393)
mouse.click(Button.left, 1)
time.sleep(1)

alttab()

# Pegar contato
mouse.position = (688, 286)
mouse.click(Button.left, 1)
time.sleep(1)

alttab()

# Colocar contato
mouse.position = (342, 239)
mouse.click(Button.left, 1)
mouse.click(Button.right, 1)
mouse.position = (417, 323)
mouse.click(Button.left, 1)
time.sleep(1)

alttab()

# Pegar data
mouse.position = (695, 326)
mouse.click(Button.left, 1)
time.sleep(1)

alttab()

# Colocar data
mouse.position = (549, 237)
mouse.click(Button.left, 1)
time.sleep(0.5)
mouse.click(Button.right, 1)
mouse.position = (669, 329)
mouse.click(Button.left, 1)
time.sleep(1)
alttab()

# Pegar hora
mouse.position = (690, 392)
mouse.click(Button.left, 1)
time.sleep(0.3)
alttab()
mouse.position = (623, 238)
mouse.click(Button.left, 1)
time.sleep(0.5)
mouse.click(Button.right, 1)
mouse.position = (725, 323)
mouse.click(Button.left, 1)
time.sleep(1)
alttab()

# Pegar protocolo
mouse.position = (691, 473)
mouse.click(Button.left, 1)
time.sleep(0.1)
alttab()
time.sleep(0.1)

# Colocar protocolo
mouse.position = (15, 281)
mouse.click(Button.right, 1)
mouse.position = (83, 369)
mouse.click(Button.right, 1)
time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type('por MKTZAP')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
alttab()


# Pegar atendimento
mouse.position = (691, 535)
mouse.click(Button.left, 1)
time.sleep(0.1)
alttab()

# Colocar atendimento
mouse.position = (15, 308)
mouse.click(Button.left, 1)
time.sleep(0.1)
mouse.click(Button.right, 1)
mouse.position = (115, 395)
mouse.click(Button.left, 1)

time.sleep(0.2)
alttab()

# Pegar natureza
mouse.position = (691, 580)
clicaresquerdo()
time.sleep(0.2)
alttab()


# Colocar natureza
time.sleep(0.8)
mouse.position = (380, 280)
mouse.click(Button.left, 1)
time.sleep(0.8)
mouse.position = (427, 446)
mouse.click(Button.left, 1)
time.sleep(0.3)
keyboard.press(Key.backspace)
keyboard.release(Key.backspace)
time.sleep(0.3)
mouse.position = (533, 421)
mouse.click(Button.left, 1)
mouse.click(Button.right, 1)
mouse.position = (593, 506)
mouse.click(Button.left, 1)
time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.5)

alttab()

# Pegar tempo de atendimento

mouse.position = (695, 659)
mouse.click(Button.left, 1)
time.sleep(0.3)
alttab()


# Colocar tempo de atendimento

mouse.position = (437, 395)
time.sleep(0.5)
clicaresquerdo()
clicardireito()
mouse.position = (496, 472)
clicaresquerdo()


'''