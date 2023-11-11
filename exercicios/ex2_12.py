# Considere a seguinte lista:
# [123, 435, 987, 1984, 2, 19, 423, -178, 320]

# Faça um programa que retorne o índice do menor e do maior valor encontrado:

# O maior valor está na posição x
# O menor valor está na posição y

lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

menor = min(lista)
maior = max(lista)

i_menor = lista.index(menor)
i_maior = lista.index(maior)

print("Posição do menor valor:", i_menor)
print("Posição do maior valor:", i_maior)