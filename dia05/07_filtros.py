# %%

import pandas as pd

df = pd.read_excel("uf_brasil.xlsx")
df

# %%
notas = [4.5, 8.75, 9.65, 3.75, 6, 7.5, 10]
notas_aprovadas = []

for i in notas:
    if i >= 7:
        notas_aprovadas.append(i)
notas_aprovadas

# %%
s_notas = pd.Series(notas)
teste = s_notas >= 7
teste

# %%
s_notas[teste]

# %%
s_notas[s_notas > s_notas.median()]

# %%

df[df["Densidade (2005)"] > 10000]

# %%

filtro = (df["Densidade (2005)"]>10000) & (df["IDH (2010)"]>700)
df[filtro]

# %%
df_idh_densidade = df[filtro].copy()

# %%
df_idh_densidade["fodase"] = 10

# %%
df_idh_densidade["PIB (2015)"] = 1