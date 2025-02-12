nome = input("Digite seu nome:\n")
idade = int(input("Digite sua idade:\n"))
altura = float(input("Digite sua altura:\n"))
peso = float(input("Digite seu peso:\n"))
estado = int(input("Estado civil: 1. Casado / 2.Solteiro\n"))

if estado == 1:
    estado = "Casado"
else:
    estado = "Solteiro"

eu = [nome, idade, altura, peso, estado]

print("Nome  : ", eu[0])
print("Idade : ", eu[1], " anos")
print("Altura: ", eu[2], "m")
print("Peso  : ", eu[3], "kg")
print("Estado Civil: ", eu[4])
