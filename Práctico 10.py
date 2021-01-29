#Práctico 10: Medición de objetos
#Se debe cargar una imagen de un plano en donde hay diferentes objetos a medir.
#El rectángulo rojo (papel glace) tiene un tamaño de 10cm por 10cm.
# Se pide hacer un programa que en forma automática usando solo las medidas conocidas sea capaz de medir algunas de las siguientes cosas :
#Ancho y alto de la tarjeta,
#Ancho y alto de la goma o
#Radio de ambas monedas.

#Se importan las siguientes librerias:
import cv2
import numpy as np

#Definición de funciones:
#Se trabaja la imagen aplicando filtrado, detección de bordes y contornos
def getContours(imagen1, imagen2, ksize, arg, Thr):
    # Como en cualquier otra señal, las imágenes también pueden contener diferentes tipos de ruido, especialmente debido a la fuente (sensor de la cámara). El filtro gaussiano se utiliza para suavizar la imagen. Este método acepta los siguientes parámetros: GaussianBlur(src, dst, ksize, sigmaX). 1 - src: un objeto Mat que representa la fuente (imagen de entrada) para esta operación. 2 - dst: un objeto Mat que representa el destino (imagen de salida) de esta operación. 3 - ksize: un objeto Size que representa el tamaño del kernel. 4 - sigmaX: una variable del tipo double que representa la desviación estándar del kernel de Gauss en la dirección X.
    imagenFiltrada = cv2.GaussianBlur(imagen1, (ksize[0], ksize[1]), cv2.BORDER_DEFAULT) #ksize = Tamaño del kernel gaussiano [anchura, altura] la altura y el ancho deben ser impares y pueden tener valores diferentes. sigmaX = Desviación estándar del kernel a lo largo del eje X (dirección horizontal).
    # Umbral simple: para cada píxel, se aplica el mismo valor de umbral. Si el valor de píxel es menor que el umbral, se establece en 0; de lo contrario, se establece en un valor máximo. La función cv.threshold se utiliza para aplicar el umbral. El primer argumento es la imagen de origen, que debería ser una imagen en escala de grises . El segundo argumento es el valor umbral que se utiliza para clasificar los valores de los píxeles. El tercer argumento es el valor máximo que se asigna a los valores de píxeles que superan el umbral. OpenCV proporciona diferentes tipos de umbral que viene dado por el cuarto parámetro de la función. El umbral básico se realiza mediante el tipo cv.THRESH_BINARY
    ret, tresh = cv2.threshold(imagenFiltrada, arg[0], arg[1], cv2.THRESH_BINARY)
    # La detección de bordes es una técnica muy utilizada que nos permite aislar los objetos y separarlos del fondo. Una vez obtenido los bordes, lo único que nos faltaría es detectar los diferentes contornos para poder contar los objetos. El proceso se divide en 4 fases que iremos realizando: 1-Convertir la imagen a escala de grises. 2-Filtrar la imagen para eliminar el ruido. 3-Aplicar el detector de bordes Canny. 4-Buscar los contornos dentro de los bordes detectados. Los parámetros necesarios son: image: Imagen de origen / entrada de una matriz n-dimensional. threshold1: Es el valor de umbral alto del gradiente de intensidad. threshold2: Es el valor de umbral bajo del gradiente de intensidad.
    bordes = cv2.Canny(tresh,Thr[0],Thr[1])
    #Los contornos se pueden explicar simplemente como una curva que une todos los puntos continuos (a lo largo del límite), que tienen el mismo color o intensidad. Los contornos son una herramienta útil para el análisis de formas y la detección y reconocimiento de objetos. Para mayor precisión, use imágenes binarias. En OpenCV, encontrar contornos es como encontrar un objeto blanco sobre un fondo negro. Así que recuerde, el objeto a buscar debe ser blanco y el fondo debe ser negro. Hay tres argumentos en la función cv2.findContours(), el primero es la imagen de origen, el segundo es el modo de recuperación de contorno, el tercero es el método de aproximación de contorno. Y genera los contornos y la jerarquía. Contours es una lista de Python de todos los contornos de la imagen. Cada contorno individual es una matriz Numpy de coordenadas (x, y) de los puntos fronterizos del objeto.
    contours, hiearchy = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #Para dibujar los contornos se utiliza la función cv2.drawContours . También se puede utilizar para dibujar cualquier forma, siempre que tenga sus puntos límite. Su primer argumento es la imagen de origen, el segundo argumento son los contornos que deben pasarse como una lista de Python, el tercer argumento es el índice de contornos (útil cuando se dibuja un contorno individual. Para dibujar todos los contornos, pase -1) y los argumentos restantes son color, grosor etc.
    dibujo = cv2.drawContours(imagen2, contours, -1, (0,255,0), 2)
    return imagenFiltrada, tresh, bordes, dibujo, contours

#Se hallan los puntos extremos de un contorno
def getExtremePoints(arg):
    extInfIzq = tuple(arg[arg[:, :, 0].argmin()][0])
    extSupDer = tuple(arg[arg[:, :, 0].argmax()][0])
    extSupIzq = tuple(arg[arg[:, :, 1].argmin()][0])
    extInfDer = tuple(arg[arg[:, :, 1].argmax()][0])
    return extInfIzq, extSupDer, extSupIzq, extInfDer

#Se realizan las diferentes mediciones
def getMiddlePointsRectangle(contourx):
    #Determinamos los puntos extremos de los contorno
    extInfIzq, extSupDer, extSupIzq, extInfDer = getExtremePoints(contourx)

    cv2.circle(dibujo2, extSupIzq, 4, (255, 0, 0), 4)
    cv2.circle(dibujo2, extInfIzq, 4, (255, 0, 0), 4)
    cv2.circle(dibujo2, extSupDer, 4, (255, 0, 0), 4)
    cv2.circle(dibujo2, extInfDer, 4, (255, 0, 0), 4)

    distX = findDis(extSupDer[0], extInfIzq[0])
    distY = findDis(extInfDer[1], extSupIzq[1])
    dist = (distX, distY)
    return dist

#Se calcula la distancia entre dos puntos
def findDis(pts1,pts2):
    return pts1 - pts2


#Inicio del programa:
imagenColor = cv2.imread('medicion_objetos.jpeg', 1)
imagenGris = cv2.imread('medicion_objetos.jpeg', 0)
imagenColorModif = cv2.imread('medicion_objetos.jpeg', 1)

#Aplicamos los filtros a la imagen cargada
imagenFiltrada1, tresh1, bordes1, dibujo1, contours1 = getContours(imagenGris, imagenColorModif, [5, 5], [138, 255], [100, 255])

#Mostramos los resultados obtenidos de trabajar la imagen paso a paso
cv2.imshow('Gaussian1', imagenFiltrada1)
cv2.imshow('Threshold1', tresh1)
cv2.imshow('Canny1', bordes1)
cv2.imshow('Contornos1', dibujo1)

minArea = 150000

for i in contours1:
    area = cv2.contourArea(i)
    #print(area)
    if area > minArea:
        # Determinamos los puntos extremos del contorno del papel rojo
        extInfIzq, extSupDer, extSupIzq, extInfDer = getExtremePoints(i)
        # Numpy array contiene los cuatro vertices del papel rojo
        puntosEntrada = np.float32([
            [extSupIzq[0], extSupIzq[1]],
            [extSupDer[0], extSupDer[1]],
            [extInfDer[0], extInfDer[1]],
            [extInfIzq[0], extInfIzq[1]]
        ])
        # Numpy array contiene los cuatro vertices del papel rojo como salida
        puntosSalida = np.float32([
            [extSupIzq[0], extSupIzq[1]],
            [extSupDer[0], extSupIzq[1]],
            [extSupDer[0], extInfIzq[1]],
            [extSupIzq[0], extInfIzq[1]]
        ])
        #En Transformación de perspectiva , podemos cambiar la perspectiva de una imagen o video determinado para obtener mejores conocimientos sobre la información requerida. En Transformación de perspectiva, necesitamos proporcionar los puntos de la imagen desde los que queremos recopilar información cambiando la perspectiva. También necesitamos proporcionar los puntos dentro de los cuales queremos mostrar nuestra imagen. Luego, obtenemos la transformación de perspectiva de los dos conjuntos de puntos dados y la envolvemos con la imagen original. Los parámetros son: 1 - src: Coordenadas de vértices cuadrangulares en la imagen de origen. 2 - dst: Coordenadas de los vértices del cuadrilátero correspondientes en la imagen de destino.
        Matrix = cv2.getPerspectiveTransform(puntosEntrada, puntosSalida)
        #Realiza deformaciones en perspectiva de la imagen de origen utilizando los coeficientes de transformación dados.
        image_transformed = cv2.warpPerspective(imagenColor, Matrix, (imagenColor.shape[1], imagenColor.shape[0]))
        # Draw circles in the founded vertices
        cv2.circle(imagenColorModif, (extSupIzq), 3, (255, 0, 0), 5)
        cv2.circle(imagenColorModif, (extInfIzq), 3, (255, 0, 0), 5)
        cv2.circle(imagenColorModif, (extSupDer), 3, (255, 0, 0), 5)
        cv2.circle(imagenColorModif, (extInfDer), 3, (255, 0, 0), 5)


#Mostramos los resultados obtenidos de trabajar la imagen paso a paso
cv2.imshow('Homografia', image_transformed)
cv2.imshow('Color', imagenColor)
cv2.imshow('Color Modificada', imagenColorModif)

#Transformamos la imagen en perspectiva a escala de grises para poder aplicar de nuevos los filtros
gray = cv2.cvtColor(image_transformed, cv2.COLOR_BGR2GRAY)
#Aplicamos los filtros a la imagen transformada en escala de grises
imagenFiltrada2, tresh2, bordes2, dibujo2, contours2 = getContours(gray, image_transformed, [11, 11], [130, 255], [120, 255])

#Mostramos los resultados obtenidos de trabajar la imagen paso a paso
cv2.imshow('Gaussian2', imagenFiltrada2)
cv2.imshow('Threshold2', tresh2)
cv2.imshow('Canny2', bordes2)
cv2.imshow('Contornos2', dibujo2)

#Imprimimos la cantidad de contornos encontrados, esto nos servirá a continuación
print(len(contours2))

for i, a in enumerate(contours2):
    #print(cv2.contourArea(a), i)
    # i = 1, goma
    if i == 1:
        dimGoma = getMiddlePointsRectangle(a)
        print('El ancho de la goma es: ', '{0:.2f}'.format(dimGoma[0] / 42.3), 'cm')
        print('El alto de la goma es:  ', '{0:.2f}'.format(dimGoma[1] / 42.3), 'cm')
    # i = 2, moneda de $1
    elif i == 2:
        diametro1 = getMiddlePointsRectangle(a)
        print('El diámetro de la moneda de 1 peso es: ', '{0:.2f}'.format(diametro1[0] / 42.3), 'cm')
    # i = 3, moneda de $0,50
    elif i == 3:
        diametro50 = getMiddlePointsRectangle(a)
        print('El diámetro de la moneda de 50 centavos es: ', '{0:.2f}'.format(diametro50[0] / 42.3), 'cm')
    # i = 4, tarjeta
    elif i == 4:
        dimTarjeta = getMiddlePointsRectangle(a)
        print('El ancho de la tarjeta es: ', '{0:.2f}'.format(dimTarjeta[0] / 42.3), 'cm')
        print('El alto de la tarjeta es:  ', '{0:.2f}'.format(dimTarjeta[1] / 42.3), 'cm')
    # i = 5, papel rojo
    elif i == 5:
        dimPapelRojo = getMiddlePointsRectangle(a)
        print('El largo en pixeles del papel rojo es:  ', dimPapelRojo[1])
        # 1cm = 42.3 pixeles
        print(dimPapelRojo[1] / 10, 'píxeles equivalen a 1 cm')

cv2.waitKey(0)