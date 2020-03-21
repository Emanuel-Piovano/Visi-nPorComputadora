import cv2
import time

img = cv2.imread('La libertad guiando al pueblo.jpg', cv2.IMREAD_COLOR)
drawing = False # true if mouse is pressed
ix, iy = -1, -1

def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (255, 255, 255), 5)

cv2.namedWindow('Imagen')
cv2.setMouseCallback('Imagen', draw)
while(True):
    cv2.imshow('Imagen', img)
    tecla = cv2.waitKey(20)
    if tecla == ord('g'):
        cv2.imwrite('La libertad guiando al pueblo-editado-.jpg', img)
        break
    elif tecla == ord('r'):
        img = cv2.imread('La libertad guiando al pueblo.jpg', cv2.IMREAD_COLOR)
    elif tecla == ord('q'):
        break
cv2.destroyAllWindows()