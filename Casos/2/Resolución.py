#importar libreria opencv
import cv2

#cargar la imagen
imagen = cv2.imread('imagen.jpg')

#cambio de resolucion con metodo resize
imagen2 = cv2.resize(imagen, (72,72), interpolation=cv2.INTER_CUBIC)

#mostrar la imagen
cv2.imshow('imagen1',imagen)
cv2.imshow('imagen2',imagen2)
cv2.waitKey(0)