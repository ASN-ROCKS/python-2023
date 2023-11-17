# %%

import pandas as pd

df = pd.read_excel("uf_brasil.xlsx")
df
# %%

df["Unidade federativa"]

# %%

df[["Unidade federativa"]]

# %%
df[["Unidade federativa"]].T

# %%
df.columns

# %%
columns = ['Unidade federativa',
           'Abreviação',
           'Área (km²)']
df[columns]

# %%

df = df.sort_values(by="Sede de governo")
df
# %%
# Linha correspondente ao índice zero
df.loc[0]

# %%
# Linha correspondente aos índices
df.loc[[0,2,4]]

# %%
# linha correspondente a possição que o dataset está ordenado
df.iloc[0:10, 2:4]
