# %%

import pandas as pd

df_pedido = pd.read_csv("../dados/pedido.csv")
df_item_pedido = pd.read_csv("../dados/item_pedido.csv")
df_produto = pd.read_csv("../dados/produto.csv")

df_item_pedido['id_pedido'] = df_item_pedido['idPedido']

# %%
df_pedido.merge(df_item_pedido, on=['idPedido'])

# %%

df_full =  df_pedido.merge(right=df_item_pedido,
                            left_on=['idPedido'],
                            right_on=['id_pedido'],
                            how="right",
                            )

# %%

df_full_bebida = df_full[df_full['descTipoItem']=='bebida']

(df_full_bebida.groupby(by=["descUF", 'descItem'])['id_pedido']
               .nunique()
               .reset_index()
               .sort_values(by=['descUF', 'id_pedido'], ascending=[True, False])
)

# %%


df_item_pedido_pedido = df_pedido.merge(df_item_pedido,
                                        left_on=['idPedido'],
                                        right_on=['id_pedido'])

df_full = df_item_pedido_pedido.merge(df_produto)

df_full
# %%

df_full = (df_pedido.merge(df_item_pedido)
                    .merge(df_produto)
                    .groupby(by=['descUF'])
                    .agg({'vlPreco':['sum', 'mean', 'median'], 
                          'idPedido':['nunique'],
                          })
                    )

df_full.columns = df_full.columns.droplevel()
df_full['ticket_medio'] = df_full['sum'] / df_full['nunique']
df_full
# %%
df_full