# %%

import pandas as pd

# %%

data = {
    "nome": ['Téo', 'Maria', 'José', 'Miguel', None],
    "idade":[31, 2, 4, 18, None],
    "sexo_nasc": ["M", "F", "M", "M", None],
    "renda": [4500., 0., 0., 1300., 500]
}

# %%
df = pd.DataFrame(data)
df

# %%

df["nome"][0]

# %%

df.describe()

# %%

df[["nome", "sexo_nasc"]] # SELECT nome, sexo_nasc FROM df

# %%
describe = df[["nome", "sexo_nasc"]].describe()

# %%
describe["sexo_nasc"]["top"]
