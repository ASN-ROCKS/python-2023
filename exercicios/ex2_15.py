# Escreva um programa que solicite ao usuário uma palavra
# e verifique se a palavra é um palíndromo
# (ou seja, é a mesma palavra quando lida de trás para frente).


palavra = input("Entre com uma palavra: ")

if palavra == palavra[::-1]:
    print("A palavra é um palíndromo!")
    
else:
    print("A palavra não é um palíndromo!")