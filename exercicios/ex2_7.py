# Faça um programa que receba um número.
# Verifique se este número é primo ou não, e retorne o resultado:
# 	O número x é primo
# ou
# 	O número x não é primo

numero = int(input("Entre com um número: "))

for i in range(2,int(numero/2)+1):
    
    if numero % i == 0:
        print("O número não é primo!")
        break
    
else:
    print("O número é primo!")