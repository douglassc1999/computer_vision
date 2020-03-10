import numpy as np
import cv2 as cv

# passe a dimensão da matriz que quer formar o gradiente
def gradiente(lin, col):
  grad = np.zeros((lin, col), dtype='int')
  grad[lin-1, :] = 256

  for l in range(1, lin):
    # usando interpolação bilinear 
    # https://en.wikipedia.org/wiki/Bilinear_interpolation
    grad[l] = ((lin - l)/(lin - (l-1)))*grad[l-1] + ((l - (l - 1))/(lin - (l-1)))*grad[lin-1]
  
  return grad

grad = gradiente(500, 355).astype('uint8')
cv.imshow('gradiente', grad)
cv.waitKey(0)
cv.destroyAllWindows()


