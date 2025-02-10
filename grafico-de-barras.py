mport matplotlib.pyplot as plt

def criar_grafico_de_barras():
    try:
        num_dados = int(input("Quantos dados você quer inserir? "))
        categorias = []
        valores = []

        for i in range(num_dados):
            categoria = input(f"Digite o nome da categoria {i+1}: ")
            valor = float(input(f"Digite o valor para {categoria}: "))
            categorias.append(categoria)
            valores.append(valor)

        plt.figure(figsize=(10, 6))
        plt.bar(categorias, valores, color='skyblue')
        plt.xlabel('Categorias')
        plt.ylabel('Valores')
        plt.title('Gráfico de Barras')
        plt.show()
    except ValueError:
        print("Erro: Certifique-se de inserir números válidos para os valores.")

criar_grafico_de_barras()
