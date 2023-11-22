# %%

import pandas as pd

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

df_produto = pd.read_csv("../dados/produto.csv")
df_produto

# %%
(df_produto.sort_values(by=['vlPreco','descItem'],
                        ascending=[False, True]))


# SELECT *
# FROM df_produto
# ORDER BY vlPreco DESC
# LIMIT 5

# %%

