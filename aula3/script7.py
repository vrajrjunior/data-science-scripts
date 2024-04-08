parcelas = [125.37, 235.79, 159.03, 235.01, 1024.55]
reajustadas = list(map(lambda x: round((x*0.04)+x,2), parcelas))
print(reajustadas)