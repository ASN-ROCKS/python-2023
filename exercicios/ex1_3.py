# Faça um programa que receba o raio de uma circunferência em centímetros.
# Retorne para o usuário qual é a área e perímetro desta circunferência no seguinte formato.

# Área:  x.xx
# Perímetro:  y.yy

raio = float(input("Entre com o raio da circunferência: "))

area = 3.14 * raio * raio
perimetro = 2 * 3.14 * raio

print("Area:", area)
print("Perimetro:", perimetro)