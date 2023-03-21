import adivinhacao
import forca
import time

def escolhe_jogo():
    print("*********************************")
    print("  Escolha um jogo para iniciar!  ")
    print("*********************************")

    while True:
        
        print("(1) Adivinhação (2) Forca (3) Sair")
        opcao = int(input("Digite a opção desejada: "))

        if (opcao == 1):
            adivinhacao.jogar()
        elif (opcao == 2):
            forca.jogar()
        elif (opcao == 3):
            print("Saindo ...")
            time.sleep(3)
            break
        else: 
            print("Opção inválida. Digite novamente.")
          
if __name__ == "__main__":
    escolhe_jogo()
