import cv2
import numpy as np

imagen=cv2.imread("images.jpeg")

#separar y unir imagenes
B,G,R=cv2.split(imagen)
unida=cv2.merge([B, G,R])
cv2.imshow('image1',B)
cv2.imshow('image2',G)
cv2.imshow('image3',R)
cv2.waitKey(0)


print(imagen.shape[:2])
negra=np.zeros(imagen.shape[:2],dtype='uint8')
cv2.imshow('Imagen1',cv2.merge([B,negra,negra]))
cv2.imshow('Imagen2',cv2.merge([negra,G,negra]))
cv2.imshow('Imagen3',cv2.merge([negra,negra,R]))
cv2.imshow('Imagen4',unida)
cv2.waitKey(0)
