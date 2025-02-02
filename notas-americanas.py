nota = float(input("Digite sua nota: "))

if nota < 6.0:
    print("Sua nota americana é equivalente a F.")
elif nota < 7.0:
    print("Sua nota americana é equivalente a D.")
elif nota < 8.0:
    print("Sua nota americana é equivalente a C.")
elif nota < 9.0:
    print("Sua nota americana é equivalente a B.")
else:
    print("Sua nota americana é equivalente a A.")
