# %%
import pandas as pd

# %%
df = pd.read_excel("uf_brasil.xlsx")
df

# %%
df.info(memory_usage='deep')

# %%
df.dtypes
