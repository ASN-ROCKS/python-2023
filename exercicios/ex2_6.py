# Refaça o exercício 2.2 utilizando for e listas para receber as notas dos alunos

notas = []

for i in range(1,5):
    notas.append(float(input(f"Entre com a nota {i}:")))
    
media = sum(notas) / len(notas)
menor = min(notas)
maior = max(notas)

print("Media:", media)
print("Menor:", menor)
print("Maior:", maior)