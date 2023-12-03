# %%

import pandas as pd
import sqlalchemy

# %%

engine = sqlalchemy.create_engine("sqlite:///../dados/database.db")

# %%

df_pedido = pd.read_sql_table("pedido", con=engine)
df_pedido
# %%

df_pedido = pd.read_sql_query("SELECT * FROM pedido", con=engine)
df_pedido

# %%

query = """
SELECT descUF,
       count(distinct idPedido) AS qtdePedido
FROM pedido
GROUP BY descUF
"""

df_uf = pd.read_sql_query(query, con=engine)
df_uf

# %%

def qtde_pedido_uf(uf, engine):
    query = f"""
    SELECT count(distinct idPedido) AS qtd
    FROM pedido
    WHERE descUF = '{uf}';
    """
    df = pd.read_sql_query(query, engine)
    df = df['qtd'].iloc[0]
    return df

# %%

qtde_pedido_uf("Rio de Janeiro", engine)
# %%

frase = "Meu nome é:{nome_pessoa}"
print(frase.format(nome_pessoa="Jessica") )
# %%

