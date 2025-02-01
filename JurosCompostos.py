valorInicial = float(input("Digite o valor inicial do montante: R$ "))
i = float(input("Rentabilidade mensal (%): "))

i = i / 100
meses = int(input("Digite o número de meses que irá deixar render: "))

valorFinal = valorInicial * (1 + i)**meses

print(f"Valor após {meses} meses: R$ {valorFinal:.2f}")
