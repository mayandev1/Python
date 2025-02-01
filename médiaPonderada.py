nota = float(input("Digite sua nota em Português:\n"))
nota2 = float(input("Digite sua nota em Inglês:\n"))
nota3 = float(input("Digite sua nota em Matemática:\n"))
nota4 = float(input("Digite sua nota em Química:\n"))
nota5 = float(input("Digite sua nota em Física:\n"))

mediaPonderada = ((nota * 1) + (nota2 * 1) + (nota3 * 3) + (nota4 * 2.5) + (nota5 * 2.5)) / 10 # a soma dos pesos é 10

print("+---------------------------------------------+")
print("Nota em Português: ", nota)
print("Nota em Inglês: ", nota2)
print("Nota em Matemática: ", nota3)
print("Nota em Química: ", nota4)
print("Nota em Física: ", nota5)
print(f"Sua média ponderada é: {mediaPonderada:.2f}")
print("+---------------------------------------------+\n")
