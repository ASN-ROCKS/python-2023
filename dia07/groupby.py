# %%

import pandas as pd

df_pedido = pd.read_csv("../dados/pedido.csv")
df_pedido

# %%

df_pedido['txtRecado'].count()

# %%

ufs = df_pedido['descUF'].unique()

freq = {}

for uf in ufs:
    df_filter = df_pedido[df_pedido['descUF'] == uf]
    freq[uf] = df_filter['idPedido'].count()

pd.Series(freq)

# %%

serie_group_by = df_pedido.groupby(by=['descUF'])['idPedido'].count()
serie_group_by = serie_group_by.reset_index().rename(columns={'idPedido':'qtdePedido'})
serie_group_by
# %%

pedido_uf = (df_pedido.groupby(by=['descUF'])['idPedido']
                      .count()
                      .reset_index()
                      .rename(columns={'idPedido':'qtdePedido'})
                      .sort_values(by="qtdePedido", ascending=False))

# %%
pedido_uf.reset_index(drop=True)

# %%

uf_ketchup = df_pedido.groupby(by=['descUF', 'flKetchup'])[['idPedido', 'dtPedido']].count()
uf_ketchup
# %%
uf_ketchup.unstack()

# %%

df_pivot = uf_ketchup.reset_index().pivot_table(values='idPedido',
                                                index='descUF',
                                                columns='flKetchup')

df_pivot['Total'] = df_pivot.sum(axis=1)

# %%
df_pivot

# %%

import random
import numpy as np

def fodase(x):
    return random.randint(x.min(), x.max())


df_stats = (df_pedido.groupby(by=['descUF'])
                     .agg({'idPedido': ['count', fodase, lambda x: np.percentile(x,0.25) ],
                           'dtPedido': ['min', 'max']}))

# %%
df_stats.columns = df_stats.columns.droplevel()
df_stats = df_stats.reset_index()
df_stats


# %%

df_pedido.groupby(by=['descUF'])[['idPedido']].describe()

# %%
