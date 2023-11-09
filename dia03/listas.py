# %%

minha_lista = ["Téo", 31, "Nah", "Maria", True]

print(minha_lista)

# %%

len(minha_lista)
# %%

minha_lista = ["Téo", 31, "Nah", "Maria", True, ["Thalita", "Amanda"] ]

len(minha_lista)

# %%

minha_lista[-1][0].upper()

# %%
minha_lista[3][-1]

# %%

minha_lista[:3]
# %%

minha_lista[::-1]

# %%
minha_lista

# %%

notas = [10, 4.5, 8.7, 9, 9.75]

media = sum(notas) / len(notas)
media

# %%
notas.append(10.75)

# %%

notas.extend([7, 5, 4.25])
# %%

notas
# %%

notas[3:3] = [1,2,3]
notas

# %%
notas