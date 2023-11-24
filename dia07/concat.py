# %%

import pandas as pd

# %%

df_1 = pd.DataFrame(
    {
        "nome": ["teo", "nah", "maria"],
        "idade": [31, 33, 2],
        "ex": [ ['ana', 'maria'], None, None ]
    }
)
df_1
# %%

df_2 = pd.DataFrame(
    {
        "sexo": ['f', 'f', 'm'],
        "idade": ['30', '23', '45'],
        "nome": ["lara", "ana", "josé"],
    }
)

df_2
# %%
dfs = pd.concat([df_1, df_2])
dfs['idade'] = dfs['idade'].astype(int)
dfs
# %%
