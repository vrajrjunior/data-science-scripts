import random as rd

palpites_restantes = 3

while palpites_restantes > 0:
  numero_aleatorio = rd.randint(0, 10)
  palpite = input('Entre com um número entre 0 e 10 ou digite "sair". Você terá 3 tentativas.\t')
  if palpite == 'sair':
    print("\nVocê saiu do programa. Até breve!!!")
    break

  if int(palpite) == numero_aleatorio:
    print("\nVocê acertou. Parabéns!!!")
    break
  else:
    print(f"\nErrou. Palpite do computador: {numero_aleatorio}\nVocê tem {(palpites_restantes - 1)} tentativa(s)\n" if (palpites_restantes - 1) > 0 else f"\nErrou. Palpite do computador: {numero_aleatorio}\nVocê perdeu todas as suas chances\n" )
    palpites_restantes -= 1
