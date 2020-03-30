#Práctico 7 - Transformación de similaridad: Se puede definir mediante la consola el desplazamiento de la imagen en x e y, un ángulo de rotación y una escala para la misma
import cv2

img = cv2.imread('La libertad guiando al pueblo.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Imagen', img)
cv2.waitKey(20)
x, y, ang, s = 0, 0, 0, 1.0


def similaridad(image, x, y, angle, scale = 1.0, center = None):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w/2, h/2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    #A los valores de la tercer columna de la matriz M, debemos sumarle el valor del desplazamiento en x e y que definimos mediante la consola
    M[0][2] += x
    M[1][2] += y
    edit = cv2.warpAffine(image, M, (w, h))
    return edit


while(True):
    cv2.imshow('Imagen', similaridad(img, x, y, ang, s))
    tecla = cv2.waitKey(20)
    if tecla == ord('e'):
        x = int(input('Defina el desplazamiento x: '))
        y = int(input('Defina el desplazamiento y: '))
        ang = int(input('Defina el ángulo: '))
        s = float(input('Defina la escala: '))
    elif tecla == ord('q'):
        break
cv2.destroyAllWindows()