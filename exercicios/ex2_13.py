# Escreva um programa que receba uma lista de números do usuário 
# e conte quantas vezes um número específico aparece na lista.
# Solicite ao usuário um número e exiba a contagem.

valores = {}
while True:
    
    valor = input("Entre com um valor: ")
    if valor == "":
        break
    
    valor = int(valor)
    
    if valor not in valores.keys():
        valores[valor] = 1
        
    else:
        valores[valor] += 1
        

valor_busca = int(input("Entre com um valor para buscar: "))

print(valores[valor_busca])