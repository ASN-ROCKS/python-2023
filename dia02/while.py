# %%

cont = 1

while cont <= 100:
    print(cont)
    cont = cont + 1

# %%

cont = 1
while cont <= 100:
    
    if cont % 2 == 0:
        print(cont)
    
    cont += 1

# %%

cont = 1
while cont <= 100:

    if cont % 2 == 0:
        print(cont)
    
    elif cont % 15 == 0:
        print("Divisivel por 15! Para!")
        break

    cont += 1
# %%

cont = 1
while cont <= 100:

    if cont % 2 == 0:
        print(cont, "par")
        cont += 1
        continue

    print(cont)
    cont += 1
# %%
cont = 1
while cont <= 100:

    if cont % 2 == 0:
        print(cont, "par")

    else:
        print(cont)
    
    cont += 1

# %%

cont = 1
while cont <= 10:

    print(cont)

    if cont % 15 == 0:
        print("Divisivel por 15, parando...")
        break
    
    cont += 1

else:
    print("Laço executado com sucesso!")

print("Fim do laço")

# %%
