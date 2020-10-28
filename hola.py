# %%
import numpy as np
import pandas as pd
'''
lista = [1,2,4,6]
nplista = np.array(lista)
pdlista = pd.Series(lista)

print(lista*2)
print(nplista*2)
print(pdlista*2)
'''
# %%

df = pd.read_csv("insurance.csv")

#print(df)

# %%
#Se le puede poner entre parentesis cuantos elementos quieres imprimir
print(df.head(10)) 
'''
df.tail()
df.sample()

df.describe()
df.info()

# %%
df[['age']]

'''
#df[10]

# %%
