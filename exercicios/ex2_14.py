# Escreva um programa que solicite ao usuário um número
# e exiba a tabuada desse número de 1 a 10.

n = int(input("Entre com um número: "))

for i in range(1,11):
    print(n, "x", i, "=", n*i)