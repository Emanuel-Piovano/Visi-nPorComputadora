#Práctica 12 - Alineación de imágenes usando SIFT:
#1. Capturar dos imágenes con diferentes vistas del mismo objeto
#2. Computar puntos de interés y descriptores en ambas imágenes
#3. Establecer matches entre ambos conjuntos de descriptores
#4. Eliminar matches usando criterio de Lowe
#5. Computar una homografía entre un conjunto de puntos y el otro
#6. Aplicar la homografía sobre una de las imágenes y guardarla en otra (mezclarla con un alpha de 50 %)

#Se importan las siguientes librerias:
import numpy as np
import cv2

#Cantidad mínima de match
MIN_MATCH_COUNT = 10

#Leer las dos imágenes
img1 = cv2.imread('imagen1.jpg')
img2 = cv2.imread('imagen2.jpg')

#Transformamos las imagenes en escala de grises
gris1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gris2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#Inicializamos el detector y el descriptor
sift = cv2.xfeatures2d.SIFT_create()

#Encontramos los puntos clave y los descriptores con SIFT en ambas imágenes
keypoints1, descriptors1 = sift.detectAndCompute(gris1, None)
keypoints2, descriptors2 = sift.detectAndCompute(gris2, None)

#Dibujamos los puntos encontrados en los puntos claves
cv2.drawKeypoints(img1, keypoints1, img1)
cv2.drawKeypoints(img2, keypoints2, img2)

matcher = cv2.BFMatcher(cv2.NORM_L2)    #El emparejador de fuerza bruta toma el descriptor de una característica en el primer conjunto y se compara con todas las demás características en el segundo conjunto utilizando algún cálculo de distancia. Y se devuelve el más cercano. Para la función cv2.BFMatcher () se necesitan dos parámetros opcionales. El primero es normType, especifica la medida de distancia que se utilizará. Por defecto, lo es cv2.NORM_L2. El segundo parámetro es una variable booleana, crossCheckque es falsa por defecto. Si es cierto, Matcher devuelve solo aquellas coincidencias con valor (i, j) de manera que el descriptor i-ésimo en el conjunto A tiene el descriptor j-ésimo en el conjunto B como la mejor coincidencia y viceversa. Es decir, las dos características de ambos conjuntos deben coincidir. Proporciona un resultado consistente y es una buena alternativa a la prueba de relación propuesta por D. Lowe en papel SIFT.

matches = matcher.knnMatch(descriptors1, descriptors2, k=2)     #Usaremos BFMatcher.knnMatch()para obtener k mejores coincidencias. En este ejemplo, tomaremos k = 2 para que podamos aplicar la prueba de razón explicada por D.Lowe en su artículo.

#Guardamos los buenos matches usando el test de razón de Lowe
good = []
for m, n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

if (len(good) > MIN_MATCH_COUNT):
    scr_pts = np.float32([keypoints1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    #Computamos la homografía con RANSAC
    H, mask = cv2.findHomography(dst_pts, scr_pts, cv2.RANSAC, 5.0)

else:
    print('No existen suficientes matchs')

#Aplicamos la transformación perspectiva H a la imagen 2
imgTrans = cv2.warpPerspective(img2, H, (600, 800))

#Mezclamos ambas imágenes
alpha = 0.5
blend = np.array(imgTrans * alpha + img1 * (1 - alpha), dtype = np.uint8)   #Se mezclan las imágenes, en las zonas de coincidencia aumenta el brillo un 50%, en cambio, en las zonas de no coincidencia, el brillo baja un 50%.
img3 = cv2.drawMatchesKnn(img1, keypoints1, img2, keypoints2, matches[:10], None, flags=0)    #La función cv2.drawMatchesKnn() nos ayuda a dibujar las coincidencias. Apila dos imágenes horizontalmente y dibuja líneas desde la primera imagen a la segunda, mostrando todas las k mejores coincidencias. Si k = 2, dibujará dos líneas de coincidencia para cada punto clave. Entonces tenemos que pasar una máscara si queremos dibujarla selectivamente.

#Mostramos los resultados obtenidos
cv2.imshow('Imagen 1', img1)
cv2.imshow('Imagen 2', img2)
cv2.imshow('Perspectiva', imgTrans)
cv2.imshow('Combinacion de imagenes', blend)
cv2.imshow('Matches', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()