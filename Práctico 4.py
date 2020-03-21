import cv2

cap = cv2.VideoCapture(0)
#Obtenemos el ancho de la imagen obtenida a través de la cámara
print('El ancho de la imagen de la cámara es:', cap.get(3))
#Obtenemos el alto de la imagen obtenida a través de la cámara
print('El alto de la imagen de la cámara es:', cap.get(4))

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is True:
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()