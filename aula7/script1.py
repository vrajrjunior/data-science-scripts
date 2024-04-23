import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

titanic = sns.load_dataset('titanic')

df = pd.DataFrame(titanic)
hist = df.hist(column='age', by='sex')
plt.show()

titanic['survived'].value_counts().plot(kind='barh')
plt.show()

titanic.boxplot(column=['age', 'fare'], grid=False, fontsize=15, rot=45)
plt.show()