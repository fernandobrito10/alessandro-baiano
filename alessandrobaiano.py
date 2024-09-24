'''
Novo atendimento: X=1320 Y=174
Colocar código do cliente: X=34 Y=239
Negar coisas 1: X=723 Y=380
Negar coisas 2: X=681 Y=393
Colocar contato: X=429 Y=238
Colocar data e hora: X=549 Y=237
Escrever atendimento: X=49 Y=284
Colocar natureza: X=378 Y=282
Colocar tempo de atendimento: X=437 Y=395
Barra para rolar: X=1254 Y=203  
Ok para finalizar atendimento: X=1335 Y=175
'''

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import time

mouse = MouseController()
keyboard = KeyboardController()

time.sleep(1)

# Novo atendimento
mouse.position = (1320, 174)
mouse.click(Button.left, 1)
time.sleep(1)

# Colocar código
mouse.position = (34, 239)
mouse.click(Button.left, 1)
keyboard.type('1')
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
# Colocar contato
mouse.position = (429, 328)
mouse.click(Button.left, 1)
keyboard.type('Cliente')
time.sleep(1)

# Colocar Data e Hora
mouse.position = (549, 237)
mouse.click(Button.left, 1)
time.sleep(1)
keyboard.type('23092024')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type('0830')
time.sleep(1)


# Escrever atendimento
mouse.position = (49, 284)
mouse.click(Button.left, 1)
keyboard.type('1886-3082814342273 por MKTZAP Cliente entrou em contato para setup ser finalizado, com acesso fiz teste de venda e estava tudo certo.')
time.sleep(1)

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