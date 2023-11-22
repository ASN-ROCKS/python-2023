# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_pedido = pd.read_csv('../dados/pedido.csv')
df_pedido

# %%
df_pedido.info()

# %%
df_pedido[df_pedido['flKetchup']==True]

# %%
df_pedido['flKetchup'].unique()

# %%
df_pedido.head(10)

# %%
df_pedido.tail(10)

# %%

df_produto = pd.read_csv('../dados/produto.csv')
df_produto

# %%
df_produto.info()

# %%
df_produto['vlPreco'].describe()

# %%
df_produto['log_vl_preco'] = np.log(df_produto['vlPreco']+1)
df_produto['sqrt_vl_preco'] = np.sqrt(df_produto['vlPreco'])
df_produto

# %%
df_produto.hist(density=True)
plt.show()

# %%
df_produto['preco_alto'] = (df_produto['vlPreco'] > df_produto['vlPreco'].mean()).astype(int)
df_produto

# %%
df_produto.shape[0] # numero de linhas do dataframe
df_produto.shape[1] # numero de colunas do dataframe

# %%
df_produto = df_produto.drop(columns=['log_vl_preco'])
df_produto

# %%
df_produto.drop(columns=['preco_alto'], inplace=True)

# %%
df_produto['descItem'].unique()

# %%

def is_name(x, name='massa'):
    return int(x.startswith(name))

df_produto['is_massa']= df_produto['descItem'].apply(is_name)
df_produto

# %%

lambda_is_massa = lambda x: x.startswith("massa")
lambda_is_massa('massa integral')

# %%

df_produto['is_cheese'] = (df_produto['descItem'].apply(lambda x: x.startswith("queijo"))
                                                 .astype(int))

df_produto

# %%

df_produto['is_tomato']= df_produto['descItem'].apply(is_name, args=('tomate',))
df_produto

# %%

df_produto.apply(lambda row: row["is_massa"] == row['is_cheese'] == row['is_tomato'] == 0, axis=1)

# %%

df_produto['vlPreco'] * df_produto['preco_alto']

# %%

df_produto["descItem"].str.startswith('massa')

# %%

def intervalo(x):
    if x < 3:
        return 'baixo'
    elif x <6:
        return 'medio'
    else:
        return 'alto'
    
df_produto['vlPreco'].apply(intervalo)
