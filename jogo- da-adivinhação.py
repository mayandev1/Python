import random

def jogoAdivinhacao():
    numeroSecreto = random.randint(1, 100)
    tentativas = 0

    while True:
        palpite = int(input("Digite um número inteiro: "))
        tentativas += 1
        
        if palpite == numeroSecreto:
            print("Parabéns!! Você venceu o jogo em", tentativas, "tentativas!")
            break
        elif palpite < numeroSecreto:
            print("Tente um número maior...")
        else:
            print("Tente um número menor...")

jogoAdivinhacao()
