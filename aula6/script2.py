import pandas as pd

mtcars = pd.read_csv('mtcars.csv', sep=',')
mtcars = mtcars.sort_values(by='hp', ascending=False)

print('Matriz ordenada')
print(mtcars)

print('\nQual o carro com mais HP?')
print(f'O carro com mais HP é o {mtcars.iloc[0,0]}, com {mtcars.iloc[0,4]}hp de potência.')

print('\nEle está muito mais a frente do segundo colocado?')
print(f'Ele tem {(mtcars.iloc[0,4] - mtcars.iloc[1,4])}hp a mais que o segundo colocado, que é o {mtcars.iloc[1,0]}, com {mtcars.iloc[1,4]}hp de potência.')

print('\nMatriz com os carros com transmissão automática.')
automaticos = mtcars[mtcars['am'] == 0]
print(automaticos)
print('\nNúmero de carros com transmissão automática utilizando o .shape')
print(automaticos.shape[0])

print('\nMatriz com os carros com motor em forma de V.')
motor_v = mtcars[mtcars['vs'] == 0]
print(motor_v)
print('\nNúmero de carros com motor em forma de V utilizando o .shape')
print(motor_v.shape[0])

print('\nAmostra com 10 elementos')
amostra = mtcars.sample(n=10, replace=True, random_state=1)
print(amostra)