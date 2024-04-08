from math import sqrt

numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

primos_raiz = {}
for x in numeros_primos:
  primos_raiz[x] = sqrt(x)
print(primos_raiz)