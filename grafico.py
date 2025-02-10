import matplotlib.pyplot as plt

def gerar_grafico(dados_x, dados_y, titulo, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.plot(dados_x, dados_y, marker='o', linestyle='-', color='b')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def main():
    
    dados_x = input("Digite os valores de X separados por vírgula: ").split(',')
    dados_y = input("Digite os valores de Y separados por vírgula: ").split(',')
    titulo = input("Digite o título do gráfico: ")
    xlabel = input("Digite o título do eixo X: ")
    ylabel = input("Digite o título do eixo Y: ")


    dados_x = [float(x) for x in dados_x]
    dados_y = [float(y) for y in dados_y]

    gerar_grafico(dados_x, dados_y, titulo, xlabel, ylabel)

if __name__ == "__main__":
    main()
