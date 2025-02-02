dinheiro = float(input("Digite o seu saldo (em R$):\n"))
precoLitros = 5.0
litros = dinheiro/precoLitros

kmPorLitro = 20.0
distancia = litros * kmPorLitro

print(f"Com R$ {dinheiro:.2f}, você pode comprar {litros:.2f} litros de combustível.")
print(f"Com {litros:.2f} litros de combustível, o carro pode andar {distancia:.2f} quilômetros.")
