frase = "Mais vale um pássaro..."
print("".join(['x' if x == 'a' or x == 'á' else x for x in frase]))

frase = "Mais vale um pássaro..."

##com o print caractere por caractere
# for caractere in frase:
#   if caractere == "a" or caractere == "á":
#     print("X", end='')
#   else:
#     print(caractere, end='')
