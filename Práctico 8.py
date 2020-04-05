#Práctico 8 - Transformación afín: Se selecciona 3 puntos en la ventana emergente que muestra una imagen. Una vez seleccionados, aparece en otra ventana una imagen superpuesta a la original en la posición que se indicó con los tres puntos
import cv2
import numpy as np

circulo = [[-3, -3], [-3, -3], [-3, -3]]
contador = 0
height2, width2 = 0, 0

def puntos(event, x, y, flags, params):
    global contador
    if event == cv2.EVENT_LBUTTONDOWN:
        circulo[contador] = x, y
        contador += 1
        print(circulo)

img1 = cv2.imread('Notebook HP.png')
img2 = cv2.imread('Ash y Pikachu.png')
while True:
    if contador == 3:
        img1 = cv2.imread('Notebook HP.png')
        height1, width1 = img1.shape[:2]
        height2, width2 = img2.shape[:2]
        pts1 = np.float32([circulo[0], circulo[1], circulo[2]])
        pts2 = np.float32([[0, 0], [width2, 0], [0, height2]])
        matriz = cv2.getAffineTransform(pts2, pts1)
        imgSal = cv2.warpAffine(img2, matriz, (width1, height1))
        #Ahora creamos una máscara del logotipo y creamos también su máscara inversa
        img2gray = cv2.cvtColor(imgSal, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Paso 1', img2gray)
        cv2.waitKey(1)
        ret, mask = cv2.threshold(img2gray, 0, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        cv2.imshow('Paso 2', mask_inv)
        cv2.waitKey(1)
        #Ahora apagamos el área del logotipo
        img1_bg = cv2.bitwise_and(img1, img1, mask = mask_inv)
        cv2.imshow('Paso 3', img1_bg)
        cv2.waitKey(1)
        #Tomamos solo la región del logotipo
        img2_fg = cv2.bitwise_and(imgSal, imgSal, mask = mask)
        cv2.imshow('Paso 4', img2_fg)
        cv2.waitKey(1)
        #Ponemos el logotipo y modificamos la imagen principal.
        dst = cv2.add(img1_bg, img2_fg)
        cv2.imshow('Imagen Salida', dst)
        cv2.waitKey(1)
        cv2.imwrite('Notebook Decorada.jpg', dst)

    for x in range(0, 3):
        cv2.circle(img1, (circulo[x][0], circulo[x][1]), 3, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Imagen Original", img1)
    cv2.setMouseCallback("Imagen Original", puntos)
    tecla = cv2.waitKey(1)
    if tecla == ord('q'):
        break
cv2.destroyAllWindows()