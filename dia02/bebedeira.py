#%%
nome = input("Entre com o seu nome: ")

idade = input("Entre com a sua idade: ")
idade = int(idade)


if 65 >= idade >= 18:
    print("Beba a vontade! Só nao vale vomitar em mim!")

elif idade > 65:
    print("Nao misture remédios com bebidas!")

elif idade < 12:
    print("Va assitir desenho")

else:
    print("Vá para casa beber leite quente!")

print("Fim")