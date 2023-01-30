# importar libreria cv
import cv2

# cargar la imagen
imagen = cv2.imread('imagen.jpg')
B,G,R = cv2.split(imagen)

imagen[:,:,0] = 0
imagen[:,:,1] = 0


# mostrar la imagen
cv2.imshow('red', imagen)
cv2.waitKey(0)

