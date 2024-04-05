frase = "Mais vale um pássaro..."
print("".join(['x' if x == 'a' or x == 'á' else x for x in frase]))
