import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        tentativas += 1

        if palpite < numero_secreto:
            print("Tente um número maior.")
        elif palpite > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            break

    if tentativas == max_tentativas:
        print(f"Fim do jogo! O número secreto era {numero_secreto}.")

jogo_adivinhacao()
