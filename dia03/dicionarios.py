# %%

meu_dict = {
    "nome": "Teo",
    "sobrenome": "Calvo",
    "idade": 31,
    0: "aleatorio",
    "exs": [{"nome":"Thalita"}, {"nome":"Amanda"}]
}

meu_dict

# %%

meu_dict["nome"]

# %%

meu_dict["exs"][0]["nome"]

# %%

meu_dict.keys()

# %%

meu_dict.values()

# %%

meu_dict.items()

# %%

meu_dict["nome"] = "Teodoro"
meu_dict

# %%

meu_dict['exs'].append({"nome": "Ana"})
meu_dict

# %%

meu_dict["exs"][0]["idade"] = 31
meu_dict["exs"][1]["idade"] = 35
meu_dict["exs"][2]["idade"] = 29
meu_dict["exs"][2]["filhos"] = ['joão', 'maria']
meu_dict