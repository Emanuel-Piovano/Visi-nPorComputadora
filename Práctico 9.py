#Práctico 9 - Homografía o Transformación Perspectiva: Se selecciona 4 puntos en la ventana emergente que muestra una imagen.
# Una vez seleccionados, aparece otra ventana mostrando la figura recortada y derecha.

import cv2
import numpy as np

circulo = [[-3, -3], [-3, -3], [-3, -3], [-3, -3]]
contador = 0

def puntos(event, x, y, flags, params):
    global contador
    if event == cv2.EVENT_LBUTTONDOWN:
        circulo[contador] = x, y
        contador += 1
        print(circulo)

img = cv2.imread('Tele.jpg')
while True:
    if contador == 4:
        width, height = 700, 350
        pts1 = np.float32([circulo[0], circulo[1], circulo[2], circulo[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matriz = cv2.getPerspectiveTransform(pts1, pts2)
        imgSal = cv2.warpPerspective(img, matriz, (width, height))
        cv2.imshow("Imagen Salida", imgSal)

    for x in range(0, 4):
        cv2.circle(img, (circulo[x][0], circulo[x][1]), 3, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Imagen Original", img)
    cv2.setMouseCallback("Imagen Original", puntos)
    tecla = cv2.waitKey(1)
    if tecla == ord('q'):
        break
cv2.destroyAllWindows()