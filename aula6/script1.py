import pandas as pd

## IMPORTANDO O CSV PARA O DATAFRAME
file_path = pd.read_csv("mtcars.csv", index_col=0)

## AGRUPANDO OS DADOS PELAS COLUNAS CYL E AM E MOSTRANDO A MÉDIA
print("------AGRUPAMENTO------")
media_grupo = file_path.groupby(['cyl','am']).mean()
print(media_grupo.sort_values(by=['wt'], ascending=False))

## PIVO TABLE
print("------PIVOT TABLE------")
tabela_dinamica = pd.pivot_table(file_path, values=['hp','mpg'], index='vs',columns='am', aggfunc='median', margins=True)
print(tabela_dinamica)

## CROSSTAB
print("------CROSSTAB------")
tabela_cross = pd.crosstab(file_path['am'], file_path['cyl'], margins=True)
print(tabela_cross)