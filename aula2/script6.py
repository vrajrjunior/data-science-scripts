from math import sqrt

a = int(input("Entre com valor de A\t"))
b = int(input("Entre com valor de B\t"))
c = int(input("Entre com valor de C\t"))

delta = (b**2)-4*(a*c)
if delta < 0:
  print("Não há solução real")
elif delta == 0:
  x1 = -b / (2 * a)
  x2 = x1
  print(f'O valor de x1 e x2 são iguais. X1: {x1} e X2: {x2}')
else:
  print(f"Valor de delta: {delta}")
  x1 = (-b+(sqrt(delta)))/(2*a)
  print(f"Valor de x1: {x1}")
  x2 = (-b-(sqrt(delta)))/(2*a)
  print(f"Valor de x2: {x2}")