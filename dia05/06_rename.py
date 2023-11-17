# %%

import pandas as pd

df = pd.read_excel("uf_brasil.xlsx")
df

# %%

# Cria uma coluna nova e deleta a antiga
df["unidade_federativa"] = df["Unidade federativa"]
df = df.drop(columns=["Unidade federativa"])
df

# %%
df = df.rename(columns={"Sede de governo": "sede_governo"})
df

# %%

def remove_string(text, badletters):
    for i in badletters:
        text = text.replace(i, "")
    return text

rename_columns = {}
for i in df.columns:
    novo_nome = i.lower()
    novo_nome = remove_string(novo_nome.replace(" ","_"), "()")
    rename_columns[i] = novo_nome

df.rename(columns=rename_columns)
