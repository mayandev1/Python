valorOriginal = float(input("Valor original: R$ "))
desconto = float(input("Valor do desconto (em %) para esse produto: "))
desconto = desconto / 100

print("Valor Original:   R$", valorOriginal)
print("Desconto Ganho:   R$", valorOriginal * desconto)
print("Valor com Desconto   R$", valorOriginal * (1-desconto))
