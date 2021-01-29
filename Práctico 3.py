#Práctico 3: Obtener el frame rate o fps usando las OpenCV. Usarlo para no tener que harcodear el delay del waitKey.

import cv2
cap = cv2.VideoCapture(0)
#Imprimimos los FPS
print('Los FPS que obtiene la cámara es:', cap.get(5))

while(True):
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if((cv2.waitKey(1) & 0xFF) == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()