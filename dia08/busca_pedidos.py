# %%
with open("pedidos_refri_uf.sql", "r") as open_file:
    query = open_file.read()

# print(query)
# %%
tipo_item = input("Entre com o tipo de item psara busca: ")
uf = input("Entre com o estado para busca: ")

# %%
query_params = query.format(desc_item=tipo_item, uf=uf)
# print(query_params)

# %%
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///../dados/database.db")
df = pd.read_sql_query(query_params, con=engine)
print(df)
