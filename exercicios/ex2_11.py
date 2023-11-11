# Faça um programa que receba um número e retorne seu fatorial.

# %%
numero = int(input("Entre com um numero para calcular o fatorial: "))

total = 1
for i in range(2, numero+1):
    total *= i

print(numero, "! = ", total, sep="")
