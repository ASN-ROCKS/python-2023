# Faça um programa com uma função que recebe uma frase.
# Para cada palavra nesta frase, inverta a ordem das letras. Exiba o resultado:

# 	Esta é a frase original

# 	atsE é a esarf lanigiro

frase = input("Entre com uma frase: ")

frase_lista = frase.split(" ")

frase_lista_invertida = []

for palavra in frase_lista:
    frase_lista_invertida.append(palavra[::-1])
    
frase_invertida = " ".join(frase_lista_invertida)
print(frase_invertida)