# Faça um programa que receba um número.
# Este número corresponde a uma posição na sequência de Fibonacci: 0, 1, 1, 2, 3, 5,...
# Exiba o número da sequência cuja posição foi informada:
# 	A posição x corresponde ao número y

n = int(input("Entre com um número da posição de fibonacci: "))

seq = [0,1]

for i in range(2, n):
    seq.append(seq[-1]+ seq[-2])
    
print(seq[n-1])