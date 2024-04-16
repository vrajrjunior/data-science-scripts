import numpy as np

matriz = np.array([[1, 2, 3, 4, 5], [7, -2, -6, 1, -2], [4, 5, -3, 3, 9],
                   [4, 6, 7, 2, -1], [8, -8, 8, -8, 9]])
## MATRIZ ##
print("\n## MATRIZ ##")
print(matriz)

## MATRIZ INVERSA
print("\n## MATRIZ INVERSA ##")
inversa = np.linalg.inv(matriz)
print(inversa)

## MATRIZ TRANSPOSTA
print("\n## TRANSPOSTA ##")
transposta = matriz.T
print(transposta)

## MATRIZ DETERMINANTE
print("\n## DETERMINANTE ##")
determinante = np.linalg.det(matriz)
print(determinante)

## MATRIZ MX, MIN, SUM, MEDIA
print("\n## MÁX, MIN, SUM, MEAN, VAR, STD ##")
maximo = matriz.max(axis=None)
print('Máximo: ', maximo)
minimo = matriz.min(axis=None)
print('Mínimo: ', minimo)
soma = matriz.sum(axis=None)
print('Somatório: ', soma)
media = matriz.mean(axis=None)
print('Média: ', media)
variancia = matriz.var(axis=None)
print('Variância: ', variancia)
desvio = matriz.std(axis=None)
print('Desvio padrão: ', desvio)

## MATRIZ DIAGONAL PRINCIPAL
print("\n## DIAGONAL PRINCIPAL ##")
diagonal = np.diag(matriz)
print(diagonal)
print('Somatório da diagonal principal: ', sum(diagonal))

## MATRIZ DIAGONAL SECUNDARIA
print("\n## DIAGONAL SECUNDÁRIA ##")
diagonal_inv = np.diag(np.fliplr(matriz))
print(diagonal_inv)
print('Somatório da diagonal secundária: ', sum(diagonal_inv))
