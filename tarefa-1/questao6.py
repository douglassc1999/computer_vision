import numpy as np
import cv2 as cv

img = cv.imread('imagens/imagensComRuido/a1.jpg')
cv.imshow('primeira imagem', img)
cv.waitKey(0)

img = img/9

for i in range(2, 10):
  img = img + cv.imread('imagens/imagensComRuido/a'+ str(i) +'.jpg')/9

cv.imshow('sem ruido', img.astype('uint8'))
cv.waitKey(0)
cv.destroyAllWindows()


