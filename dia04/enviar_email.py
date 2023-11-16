# %%

arquivo = open("emails.txt", "r")
conteudo = arquivo.read()
arquivo.close()

conteudo

# %%

# %%

with open("emails.txt", "r") as open_file:
    conteudo = open_file.read()

conteudo

# %%

with open("emails.txt", "r") as open_file:
    conteudo = open_file.readlines()

conteudo

# %%

with open("emails.txt", "r") as open_file:
    conteudo = open_file.read()

conteudo.split("\n")
