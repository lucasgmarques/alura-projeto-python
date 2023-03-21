import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 100

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print(f'Tentativa {rodada} de {total_tentativas}')
        numero_digitado = int(input("Digite um número entre 1 e 100: "))

        if (numero_digitado < 1 or numero_digitado > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acerto = numero_digitado == numero_secreto
        maior = numero_digitado > numero_secreto
        menor = numero_digitado < numero_secreto

        if (acerto):
            print(f'Parabéns! Você acertou e fez {pontos} pontos!!')
            break
        else:
            if(maior):
                print("Você digitou um número maior que o número secreto!")
                if (rodada == total_tentativas):
                    print(f'O número secreto era {numero_secreto}. Você fez {pontos} pontos!')
            elif(menor):
                print("Você digitou um número menor que o número secreto!")
                if (rodada == total_tentativas):
                    print(f'O número secreto era {numero_secreto}. Você fez {pontos} pontos!')

            pontos_perdidos = abs(numero_secreto - numero_digitado)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if __name__ == "__main__":
    jogar()
