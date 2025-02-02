# divirta-se ;)
import os

def exibirTabuleiro(tabuleiro):
    print("+-----+-----+-----+")
    for linha in tabuleiro:
        print("|  " + "  |  ".join(linha) + "  |")
        print("+-----+-----+-----+")

def verificarVitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(s == jogador for s in linha):
            return True
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    return False

def verificaEmpate(tabuleiro):
    return all(all(c != " " for c in linha) for linha in tabuleiro)

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def jogoDaVelha():
    while True:
        tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        jogadorAtual = "X"
        while True:
            limparTela()
            exibirTabuleiro(tabuleiro)
            linha = int(input(f"Jogador {jogadorAtual}, digite a linha (0-2): "))
            coluna = int(input(f"Jogador {jogadorAtual}, digite a coluna (0-2): "))

            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogadorAtual
            else:
                print("Espaço já ocupado! Tente novamente.")
                continue
            if verificarVitoria(tabuleiro, jogadorAtual):
                limparTela()
                exibirTabuleiro(tabuleiro)
                print(f"Jogador {jogadorAtual} venceu!")
                break
            if verificaEmpate(tabuleiro):
                limparTela()
                exibirTabuleiro(tabuleiro)
                print("Empate!")
                break

            jogadorAtual = "O" if jogadorAtual == "X" else "X"

        jogarNovamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogarNovamente != 's':
            print("Obrigador por jogar! :)")
            break

jogoDaVelha()
