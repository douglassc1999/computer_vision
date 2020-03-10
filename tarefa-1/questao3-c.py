import numpy as np
import cv2 as cv

img = cv.imread('imagens/catiorrinho.jpg')
flip = np.fliplr(img)

result = 0.5*img + 0.5*np.fliplr(img)
result = result.astype('uint8')
cv.imshow('blending', result)
cv.waitKey(0)
cv.destroyAllWindows()



