import cv2
import numpy as np



image=cv2.imread("images.jpeg")
path=r'images.jpeg'
img=cv2.imread(path,0)

loga=np.zeros(img.shape,img.dtype)
pot=np.zeros(img.shape,img.dtype)
pot2=np.zeros(img.shape,img.dtype)

c=1
g=0.5
g2=1.5

loga=c*np.log(1+img)
maxi=np.amax(loga)
loga=np.uint8(loga/maxi*255)

pot=c*np.power(img,g)
maxi=np.amax(pot)
pot=np.uint8(pot/maxi*255)

pot2=c*np.power(img,g2)
maxi=np.amax(pot2)
pot2=np.uint8(pot2/maxi*255)

cv2.imshow('imagen1',image)
cv2.imshow('imagen2',cv2.hconcat([loga,pot]))
cv2.imshow('imagen3',cv2.hconcat([pot,pot2]))

cv2.waitKey(0)
cv2.destroyAllWindows()
exit()