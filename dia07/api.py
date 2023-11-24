# %%
import requests
import pandas as pd
import time

def etl(df):
    return df

dfs = []
for i in range(10):

    url = "https://api.opendota.com/api/proMatches"

    resp = requests.get(url)
    data = resp.json()

    df = pd.DataFrame(data)

    df = etl(df)

    dfs.append(df)
    time.sleep(10)

df_full = pd.concat(dfs)
df_full