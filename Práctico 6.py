#Práctico 6 - Rotación + Traslación (o Transformación Euclidiana): Se puede definir mediante la consola el desplazamiento de la imagen en x e y y un ángulo de rotación
import cv2

img = cv2.imread('La libertad guiando al pueblo.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Imagen', img)
cv2.waitKey(20)
x, y, ang = 0, 0, 0


def euclidiana(image, x, y, angle, center = None, scale = 1.0):
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
    cv2.imshow('Imagen', euclidiana(img, x, y, ang))
    tecla = cv2.waitKey(20)
    if tecla == ord('e'):
        x = int(input('Defina el desplazamiento x: '))
        y = int(input('Defina el desplazamiento y: '))
        ang = int(input('Defina el ángulo: '))
    elif tecla == ord('q'):
        break
cv2.destroyAllWindows()