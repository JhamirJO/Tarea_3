# importar libreria cv
import cv2

# cargar la imagen
imagen = cv2.imread('imagen.jpg')

# ROTACIÓN
imagen2 = cv2.rotate(imagen, cv2.ROTATE_90_CLOCKWISE)


# mostrar la imagen
cv2.imshow('imagen1', imagen)
cv2.imshow('imagen2', imagen2)
cv2.waitKey(0)
