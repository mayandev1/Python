tabuada = int(input("Digite um numero para ver a sua tabuada:\n"))
operador = input("Digite qual operador (+, -, *, /):\n")

if operador == "+":
    for i in range(1,11):
        print(tabuada + i)

elif operador == "-":
    for i in range(1,11):
        print(tabuada - i)
        
elif operador == "*":
    for i in range(1,11):
        print(tabuada * i)
        
elif operador == "/":
    for i in range(1,11):
        print(tabuada / i)

else:
    print("Operador inválido!")
