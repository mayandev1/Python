def calculadora():
    num = float(input("Digite o primeiro numero:\n"))
    operador = input("Digite a operação que deseja (+ - * /):\n")
    num2 = float(input("Digite o segundo numero:\n"))

    if operador == "+":
        resultado = num + num2
    elif operador == "-":
        resultado = num - num2
    elif operador == "*":
        resultado = num * num2
    elif operador == "/":
        resultado = num / num2
    else:
        print("Operador Inválido!")

    print("O resultado de", num, operador, num2, "é: ", resultado)
calculadora()
