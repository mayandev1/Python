def conversorCelsius(farenheit):
    celsius = 5/9 * (farenheit - 32)
    return celsius

farenheit = float(input("Digite sua temperatura em Farenheit:\n"))
celsius = conversorCelsius(farenheit)

print(f"{farenheit:.2f}°F é equivalente a {celsius:.2f}°C.")
