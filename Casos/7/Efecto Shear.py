# importamos las librerias
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Cargar la imagen
img = cv2.imread("imagen.jpg")

# convertir de BGR a RGB para que podamos trazar usando matplotlib
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# deshabilitar el eje x e y
plt.axis('off')

# mostrar la imagen
plt.imshow(img)
plt.show()

# obtenemos la forma de la imagen
rows, cols, dim = img.shape

# transformacion de la matriz para el Shearing
# shearing aplicado al eje x
M = np.float32([[1, 0.5, 0],
                [0, 1, 0],
                [0, 0, 1]])


# shearing aplicado al eje y
M = np.float32([[1, 0, 0],
                [0.5, 1, 0],
                [0, 0, 1]])
# aplicar una transformación de perspectiva a la imagen
sheared_img = cv2.warpPerspective(img, M, (int(cols * 1.5), int(rows * 1.5)))

# deshabilitar el eje x e y
plt.axis('off')

# mostrar la imagen resultante
plt.imshow(sheared_img)
plt.show()

# guardar la imagen resultante en el disco
plt.imsave("images-sheared.jpg", sheared_img)