import cv2

img = cv2.imread('La libertad guiando al pueblo.jpg', cv2.IMREAD_COLOR)
x1, y1, x2, y2 = -1, -1, 1, -1

def draw(event, x, y, flags, param):
    global x1, y1, x2, y2
    if event == cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        x2, y2 = x, y
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
        return (x1, x2, y1, y2)

cv2.namedWindow('Imagen')
cv2.setMouseCallback('Imagen', draw)
while(True):
    cv2.imshow('Imagen', img)
    tecla = cv2.waitKey(20)
    if tecla == ord('g'):
        print('x1:', x1, 'x2:', x2, 'y1:', y1, 'y2:', y2)
        img = cv2.imread('La libertad guiando al pueblo.jpg', cv2.IMREAD_COLOR)
        if (y2 >= y1) & (x2 >= x1):
            crop_img = img[y1:y2, x1:x2]
        elif (y2 >= y1) & (x2 < x1):
            crop_img = img[y1:y2, x2:x1]
        elif (y2 < y1) & (x2 >= x1):
            crop_img = img[y2:y1, x1:x2]
        else:
            crop_img = img[y2:y1, x2:x1]
        cv2.imshow('Imagen recortada', crop_img)
        cv2.waitKey(0)
        cv2.imwrite('La libertad guiando al pueblo-editado-.jpg', crop_img)
        break
    elif tecla == ord('r'):
        img = cv2.imread('La libertad guiando al pueblo.jpg', cv2.IMREAD_COLOR)
    elif tecla == ord('q'):
        break
cv2.destroyAllWindows()