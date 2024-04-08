a = int(input("Entre com valor de A\t"))
b = int(input("Entre com valor de B\t"))
c = int(input("Entre com valor de C\t"))

delta = (b**2)-4*(a*c)
if delta < 0:
  print("Não há solução real")
else:
  print(f"Valor de delta: {delta}")
  x1 = (-b+(delta**(1/2)))/(2*a)
  print(f"Valor de x1: {x1}")
  x2 = (-b-(delta**(1/2)))/(2*a)
  print(f"Valor de x2: {x2}")