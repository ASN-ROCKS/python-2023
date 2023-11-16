# %%

import requests

url = "https://api.nobelprize.org/2.1/nobelPrizes"

resposta = requests.get(url)

# %%
data = resposta.json()

# %%

import json

with open('fodase.json', 'w') as open_file:
    json.dump(data, open_file)


# %%

url = "https://api.opendota.com/api/proMatches"
data = requests.get(url).json()

import pandas as pd

pd.DataFrame(data)

# %%

url = "https://api.opendota.com/api/matches/7439532699"
data = requests.get(url).json()
data
# %%

import auto
# %%


# %%

golf = auto.Car("Teizinho", "prata")

# %%

auto.fodase()

# %%

import urllib.request
urllib.request.urlretrieve("ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/RDAC2301.dbc", 'RDAC2301.dbc')

