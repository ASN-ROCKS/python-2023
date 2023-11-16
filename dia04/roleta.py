import random


def valida_entrada():
    numero = 0
    while numero > 15 or numero < 1:
        try:
            numero = int(input("Entre com uma tentativa entre 1 e 15: "))
        except ValueError:
            print("Entre com um número válido em formato numérico!!!")
    return numero


sorte = random.randint(1,15)
for i in range(3):

    numero = valida_entrada()
    
    if sorte == numero:
        print("Você acertou!")
        break
    elif numero > sorte:
        print("Muito alto! Tente um número menor!")
    else:
        print("Muito baixo! Tente um número maior!")

    print("Restam", 3 - i, "tentativas!\n")