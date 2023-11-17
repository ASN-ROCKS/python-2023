# %%
import pandas as pd

# %%
df = pd.read_clipboard()
df

# %%
df = pd.read_html("https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil")

# %%
df_uf = df[1]

# %%
df_uf.to_csv("uf_brasil.csv", sep=";")

# %%
df_uf.to_excel("uf_brasil.xlsx")

# %%
df_uf.to_parquet("uf_brasil.parquet")

# %%
df_read_uf = pd.read_parquet("uf_brasil.parquet")
df_read_uf

# %%
df_uf

# %%

pedido = pd.read_csv("../dados/pedido.csv")
pedido