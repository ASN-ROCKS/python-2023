# Faça um programa que receba um número em segundos,
# converta esse número para horas, minuto e segundos. Exemplos:

# Entrada: 556
# Saída: 0:9:16

# Entrada: 140153
# Saída: 38:55:53

# %%
segundos = input("Entre com um número em segundos: ")
segundos = int(segundos)
# %%

horas = int(segundos / 3600)
# print(horas)

segundos = segundos % 3600
# print(segundos)

minutos = segundos // 60
# print(minutos)

segundos = segundos % 60
# print(segundos)

print(horas, minutos, segundos, sep=":")