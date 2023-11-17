# %%

import pandas as pd

# %%

pd.Series()

# %%

notas = [3.4, 6.5, 9.75, 6.32]

notas = pd.Series(notas)

# %%
notas.mean()

# %%
notas.max()

# %%
notas.median()

# %%
notas * 2

# %%
notas[1]

# %%
notas.index

# %%
notas_ordenadas = notas.sort_values()

# %%
notas

# %%
notas_ordenadas.reset_index(drop=True)

# %%
notas.describe()