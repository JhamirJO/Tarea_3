
# importar libreria cv
import cv2
import numpy as np

# cargar la imagen y la mostramos
imagen = cv2.imread('imagen.jpg')

cv2.imshow('imagen1', imagen)


#creamos la máscara circular y la mostramos

circular_mask = np.zeros(imagen.shape[:2], dtype='uint8')
cv2.circle(circular_mask, (155,200),190,255,-1)
cv2.imshow('Mascara circular',circular_mask)


#aplicar la máscara
masked = cv2.bitwise_and(imagen, imagen, mask = circular_mask)
cv2.imshow('Resultado', masked)
cv2.waitKey(0)





