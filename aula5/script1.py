import numpy as np

matriz = np.array([[1, 2, 3, 4, 5], [7, -2, -6, 1, -2], [4, 5, -3, 3, 9],
                   [4, 6, 7, 2, -1], [8, -8, 8, -8, 9]])
print(matriz)

## MATRIZ INVERSA
inversa = np.linalg.inv(matriz)
print(inversa)

## MATRIZ TRANSPOSTA
transposta = matriz.T
print(transposta)

## MATRIZ DETERMINANTE
determinante = np.linalg.det(matriz)
print(determinante)

## MATRIZ MX, MIN, SUM, MEDIA
maximo = matriz.max(axis=None)
print('Máximo: ', maximo)
minimo = matriz.min(axis=None)
print('Máximo: ', minimo)
soma = matriz.sum(axis=None)
print('Máximo: ', soma)
media = matriz.mean(axis=None)
print('Máximo: ', media)
variancia = matriz.var(axis=None)
print('Variância: ', variancia)
desvio = matriz.std(axis=None)
print('Desvio padrão: ', desvio)

## MATRIZ DIAGONAL PRINCIPAL
diagonal = np.diag(matriz)
print(diagonal)
print('Somatório da diagonal principal: ', sum(diagonal))

## MATRIZ DIAGONAL SECUNDARIA
diagonal_inv = np.diag(np.fliplr(matriz))
print(diagonal_inv)
print('Somatório da diagonal secundária: ', sum(diagonal_inv))
