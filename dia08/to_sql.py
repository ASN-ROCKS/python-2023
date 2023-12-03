# %%

import pandas as pd
import sqlalchemy

#%%
df = pd.DataFrame(
    {
        "nome": ["teo", "maria", "jose"],
        "idade": [31,2,4],
     }
)

df

# %%
engine = sqlalchemy.create_engine("sqlite:///../dados/database.db")

# %%
df.to_sql("tb_fodase", con=engine, index=False)

# %%
df.to_sql("tb_fodase", con=engine, index=False, if_exists='replace')

# %%
df.to_sql("tb_fodase", con=engine, index=False, if_exists='append')
