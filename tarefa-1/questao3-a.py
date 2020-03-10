"""**3 - Escreva um programa para:** <br/>
  **a - abrir uma imagem e exibir na tela os 3 canais separadamente**
"""

import numpy as np
import cv2 as cv

img = cv.imread('imagens/catiorrinho.jpg')

# Lembre que o import no opencv vem no padrao BGR

B, G, R = cv.split(img)

cv.imshow('original', img)
cv.waitKey(0)

print(img.shape)

# Temos que adicionar no canal certo
zeros = np.zeros((567,1110, 3)) # Matriz tridimensional

zeros[:, :, 1] += G  # Adiciona ao canal verde (BGR)
r1 = zeros.astype('uint8')
cv.imshow('verde', r1)
cv.waitKey(0)

zeros = np.zeros((567,1110, 3)) # Matriz tridimensional
zeros[:, :, 0] += B  # Adiciona ao canal verde (BGR)

r2 = zeros.astype('uint8')
cv.imshow('azul', r2)
cv.waitKey(0)

zeros = np.zeros((567,1110, 3)) # Matriz tridimensional
zeros[:, :, 2] += R  # Adiciona ao canal verde (BGR)
r3 = zeros.astype('uint8')
cv.imshow('vermelho', r3)
cv.waitKey(0)

cv.destroyAllWindows()

