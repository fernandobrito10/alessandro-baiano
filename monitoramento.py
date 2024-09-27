import cv2
import numpy as np
import pytesseract
from mss import mss

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def monitorar_tela(lista, intervalo = 1):
    with mss() as sct:
        monitor = sct.monitors[1]
        encontrado = False
        
        while not encontrado:
            sct_img = sct.grab(monitor)
            img = np.array(sct_img)
            imagem_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, imagem_binarizada = cv2.threshold(imagem_cinza, 150, 255, cv2.THRESH_BINARY)
            #kernel = np.ones((3, 3), np.uint8)
            #imagem_limpa = cv2.morphologyEx(imagem_binarizada, cv2.MORPH_OPEN, kernel)
            imagem_redimensionada = cv2.resize(imagem_cinza, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            #cv2.imwrite('imagem_redimensionada.png', imagem_redimensionada)

            texto = pytesseract.image_to_string(imagem_redimensionada, lang='por')

            if any(palavra in texto for palavra in lista):
                encontrado = True

    return encontrado