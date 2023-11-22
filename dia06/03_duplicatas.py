# %%

import pandas as pd
pd.set_option('display.max_rows', 100)

df_produto = pd.read_csv("../dados/produto.csv")
df_produto

# %%

df_produto['tipo_item'] = df_produto['descItem'].apply(lambda x: x.split()[0])

(df_produto.sort_values(by=['vlPreco', 'descItem'],
                       ascending=[False, True])
          .drop_duplicates(subset=['tipo_item'], keep='first'))