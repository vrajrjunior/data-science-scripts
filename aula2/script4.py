tabuada = int(input("Informe o valor para gerar a(s) tabuada(s):\t"))
for x in range(tabuada):
  print(f"\n\nTabuada do {(x+1)}\n")
  for y in range(10):
    print(f"{(x+1)} X {(y+1)} = {(x+1) * (y+1)}")
