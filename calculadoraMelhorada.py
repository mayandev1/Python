def soma():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("Soma:\n", num1 + num2)

def subtracao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("Subtração:\n", num1 - num2)

def multiplicacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("Multiplicação:\n", num1 * num2)

def divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("Divisão:\n", num1/num2)

def exponenciacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("Exponencição:\n", num1 ** num2)

opcao = 1

while opcao != 6:
    print("+=====CALCULADORA SIMPLES=====+")
    print("1. SOMA")
    print("2. SUBTRAÇÃO")
    print("3. MULTIPLICAÇÃO")
    print("4. DIVISÃO")
    print("5. EXPONENCIAÇÃO")
    print("6. SAIR")
    print("+=============================+\n")
    opcao = int(input("Sua Opção: "))

    if (opcao == 1):
        soma()
    elif (opcao == 2):
        subtracao()
    elif (opcao == 3):
        multiplicacao()
    elif (opcao == 4):
        divisao()
    elif (opcao == 5):
        exponenciacao()
    elif (opcao == 6):
        print("Encerrando programa...")
    else:
        print("Opção Inválida!")
