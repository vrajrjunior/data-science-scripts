class Operacoes:

  def __init__(self, n_1, n_2):
    self.val1 = n_1
    self.val2 = n_2

  def adicao(self):
    return f'{self.val1} + {self.val2} = {(self.val1 + self.val2)}'

  def subtracao(self):
    return f'{self.val1} - {self.val2} = {(self.val1 - self.val2)}'

  def multiplicacao(self):
    return f'{self.val1} * {self.val2} = {(self.val1 * self.val2)}'
  
  def divisao(self):
    return f'{self.val1} / {self.val2} = {(self.val1 / self.val2)}'


######
##Chamando a classe no proprio arquivo
######
operacoes = Operacoes(10,20)

print('Adição:', operacoes.adicao())
print('Subtração:', operacoes.subtracao())
print('Multiplicação:', operacoes.multiplicacao())
print('Divisão:', operacoes.divisao())

