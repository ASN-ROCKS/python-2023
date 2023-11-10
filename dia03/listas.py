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
notas.remove(10)

# %%
notas
# %%

numeros_1 = [1,2,3,4]
numeros_2 = [5,6,7]

numeros = numeros_1 + numeros_2
numeros

# %%

nomes = ["Let", "Teo", "George", "Amanda", "Nah"]

i = 0
while i < len(nomes):
    print( nomes[i].upper() )
    i += 1

# %%
for i in range(0,len(nomes)):
    print(nomes[i].upper())

# %%

for i in nomes:
    print(i.upper())

# %%

nomes = ['LeT', 'TéO', 'GeoRGe', 'AmANda', 'NaH']
nomes_corretos = []

for i in nomes:
    i = i.lower().replace("é", "e").replace("ç", 'c')
    nomes_corretos.append(i)

nomes_corretos

