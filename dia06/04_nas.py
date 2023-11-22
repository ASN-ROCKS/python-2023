# %%
import pandas as pd

df_pedido = pd.read_csv("../dados/pedido.csv")
df_pedido

# %%

df_pedido.isna().mean()

# %%

df_pedido['flKetchup'] = df_pedido['flKetchup'].fillna(False)
df_pedido

# %%
df_pedido.dropna(subset=['flKetchup', 'txtRecado'], how='any')