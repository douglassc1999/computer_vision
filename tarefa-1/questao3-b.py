import numpy as np
import cv2 as cv

img = cv.imread('imagens/catiorrinho.jpg')
cv.imshow('original', img)
cv.waitKey(0)

"""**b - Abrir uma imagem e exibir na tela a imagem invertida horizontalmente**"""

horizontal_img = np.fliplr(img)
cv.imshow('flip-horizontal', horizontal_img)
cv.waitKey(0)
cv.destroyAllWindows()


