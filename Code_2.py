import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

entorno_img = cv.imread('prueba.png', cv.IMREAD_UNCHANGED)
objetivo_img = cv.imread('taipan.png', cv.IMREAD_UNCHANGED)

resultado = cv.matchTemplate(entorno_img, objetivo_img, cv.TM_CCOEFF_NORMED)

limite_comparacion = 0.95
locacion = np.where(resultado >= limite_comparacion)
locacion = list(zip(*locacion[::-1]))
print(locacion)

if locacion:
    print('Objetivo encontrado')

    objetivo_w = objetivo_img.shape[1]
    objetivo_h = objetivo_img.shape[0]
    color_linea = (0, 255, 0)
    line_type = cv.LINE_4

    # Ocupo hacer una rutina para que pueda matchear todos los resultados posibles
    for loc in locacion:
        # Determinar la caja de posiciones
        top_left = loc
        bottom_right = (top_left[0] + objetivo_w, top_left[1] + objetivo_h)
        #Dibujar el rectangulo
        cv.rectangle(entorno_img, top_left, bottom_right, color_linea, line_type)

    cv.imshow('Compatibles', entorno_img)
    cv.waitKey()  

else:
    print('Objetivo no encontrado')