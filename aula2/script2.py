numeros = []
while True:
  valor = input("Entre com um número inteiro ou para sair digite qualquer número negativo\t")
  if int(valor) < 0:
    print("\nAté breve!!!\n")
    break
  numeros.append(int(valor))
    
print(f"Números inseridos: {numeros}")
print(f"Soma dos valores inseridos: {sum(numeros)}")
print(f"Media dos valores inseridos: {(sum(numeros) / len(numeros))}")
