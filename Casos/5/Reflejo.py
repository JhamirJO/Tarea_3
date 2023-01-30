# importar libreria cv
import cv2

# cargar la imagen
imagen = cv2.imread('imagen.jpg')

# reflejo
imagen2 = cv2.flip(imagen, 1)


# mostrar la imagen
cv2.imshow('imagen1', imagen)
cv2.imshow('imagen2', imagen2)
cv2.waitKey(0)