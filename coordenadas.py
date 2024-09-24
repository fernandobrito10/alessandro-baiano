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


import pyautogui
import time

# Exibir a posição do mouse a cada segundo
try:
    while True:
        # Obter a posição do mouse
        x, y = pyautogui.position()
        print(f"Posição atual do mouse: X={x} Y={y}")
        time.sleep(1)  # Esperar 1 segundo antes de atualizar
except KeyboardInterrupt:
    print("Programa encerrado")
