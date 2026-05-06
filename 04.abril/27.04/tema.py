import random
import time

numeros_possiveis = [1,2,3,4,5,6,7,8,9,10]

lista_de_cartas = []
def jogo():
    cartas_iniciais = 2

    while cartas_iniciais > 0:
        carta = random.choice(numeros_possiveis)
        lista_de_cartas.append(carta)
        cartas_iniciais -=1

    print("\n========================================================================= Jogo de Cartas: 21 ================================================================================")
    print("O seu objetivo é chegar o mais próximo possivel de 21 com cartas aleatórias.\n")
    while True:

        print(f"Suas cartas inciais: {lista_de_cartas}. Soma total: {sum(lista_de_cartas)}")
        if sum(lista_de_cartas) > 21:
            print(f"O número passou de 21. Fim de jogo\nSeu resultado: {sum(lista_de_cartas)}")
            break

        if sum(lista_de_cartas) == 21:
            print("A soma de suas cartas é igual a 21! Fim de jogo")
            break

        comprar_ou_parar = input("Comprar ou parar?s\nC/P: ")

        match comprar_ou_parar.upper():
            case "C":
                sorteia_carta()
                continue
            case "P":
                print(f"Fim de jogo. Resultado final: {sum(lista_de_cartas)}")
                break
            case _:
                print("Opção inválida. Tente novamente")
                continue

def sorteia_carta():
    carta = random.choice(numeros_possiveis)
    lista_de_cartas.append(carta)

jogo()