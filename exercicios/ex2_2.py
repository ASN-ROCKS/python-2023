# Faça um programa que receba 4 notas de um aluno.
# Retorne a média dessas notas, a menor e a maior nota:

# Média: x
# Menor: y
# Maior: z

nota1 = float(input("Entre com a nota 1: "))
nota2 = float(input("Entre com a nota 2: "))
nota3 = float(input("Entre com a nota 3: "))
nota4 = float(input("Entre com a nota 4: "))

notas = [nota1, nota2, nota3, nota4]

media = sum(notas) / len(notas)
menor = min(notas)
maior = max(notas)

print("Média:", media)
print("Menor:", menor)
print("Maior:", maior)