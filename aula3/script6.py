def calcula(lista):
  return (max(lista), min(lista), sum(lista), (sum(lista)/len(lista)))

maior, menor, soma, media = calcula([1, 2, 3, 4, 5])
print('Maior:', maior)
print('Menor:', menor)
print('Soma.:', soma)
print('Média:', media)