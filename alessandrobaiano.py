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
import os
import time



load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Atendimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)

def contar_atendimentos():
    return Atendimento.query.count()

with app.app_context():
    total_atendimentos = contar_atendimentos()
    print(f'Total de atendimentos: {total_atendimentos}')

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

def ctrlv():
    mouse.click(Button.right, 1)
    mouse.position = (80, 325)
    mouse.click(Button.left, 1)




time.sleep(1)



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
ctrlv()
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
mouse.position = (688, 354)
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
mouse.position = (689, 410)
time.sleep(0.3)
mouse.click(Button.left, 1)
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

'''

# Colocar natureza
time.sleep(1)
mouse.position = (378, 282)
mouse.click(Button.left, 1)
time.sleep(1)
keyboard.type('SAIDA')
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

# Colocar tempo de atendimento
time.sleep(1)
mouse.position = (437, 395)
time.sleep(1)
mouse.click(Button.left, 1)
keyboard.type('003000')
'''