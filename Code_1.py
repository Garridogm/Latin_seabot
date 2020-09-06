import cv2 as cv
import numpy as np

entorno_img = cv.imread('prueba.png', cv.IMREAD_REDUCED_COLOR_2)
objetivo_img = cv.imread('taipan.png', cv.IMREAD_REDUCED_COLOR_2)

resultado = cv.matchTemplate(entorno_img, objetivo_img, cv.TM_CCOEFF_NORMED)

# Te da la posicicon del mejor resultado

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(resultado)

print('Mejor resultado top left posiciotn %s' % str(max_loc))
print('Mejor coincidencia: %s' % max_val)

coincidencia= 0.5

if max_val >= coincidencia:
    print('Objetivo encontrado')
    
    # Me da las dimenciones del objetivo
    objetivo_w = objetivo_img.shape[1]
    objetivo_h = objetivo_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + objetivo_w, top_left[1] + objetivo_h) 

    cv.rectangle(entorno_img, top_left, bottom_right, color=(0,255,0), thickness=2, lineType=cv.LINE_4)
    
    #cv.imshow('Resultado', entorno_img)   # Muestra ventana con el resultado del estudio
    #cv.waitKey() # Se detendra el programa cuando apriete una tecla
    cv.imwrite('resultado.png', entorno_img)

else:
    print('Objetivo no encontrado.')