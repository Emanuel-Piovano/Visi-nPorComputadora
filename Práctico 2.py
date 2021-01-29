#Práctico 2: Segmentando una imagen: Crear un programa que lea una imagen realice un binarizado de la imagen aplicando un umbral. Guarde el resultado en otra imagen.

import cv2

#Leemos una imagen
img = cv2.imread('hoja.png', 0)
#Medimos la longitud de las filas y columnas del array img
(height, width) = img.shape[:2]
#Definimos que todo valor menor a 240 en el array, va a tomar el valor 0, o sea negro. Los valores mayores a 240 van a seguir teniendo su valor original
for y in range(0, height):
    for x in range(0, width):
        if img[x][y] < 240:
            img[x][y] = 0
        else:
            img[x][y] = 255
#Generamos una nueva imágen a partir del array modificado
cv2.imwrite('resultado.png', img)