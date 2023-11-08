# %%

x = "Ola mundo!"

for i in x:
    print(i)

# %%

for i in range(1,101):
    print(i)

# %%
for i in range(1,101):
    if i % 2 == 0:
        print(i)
# %%

for i in range(1,11):
    if i % 2 == 0:
        print(i)

    elif i % 15 == 0:
        break
else:
    print("Laco executado com sucesso!")
# %%

numero = -1
while numero < 1 or numero > 10:
    numero = int(input("Entre com um valor entre 1 e 10: "))

# %%

numero = -1

for i in range(3):
    if numero < 1 or numero > 10:
        numero = int(input("Entre com um valor entre 1 e 10: "))
    else:
        break

# %%

nome = ""
while 'calvo' not in nome:
    nome = input("Qual o seu nome")

# %%
