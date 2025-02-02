def GerenciadorTarefas():
    tarefas = []

    while True:
        print("+----- GERENCIADOR DE TAREFAS -----+")
        print("1 - Adicionar tarefa")
        print("2 - Deletar tarefa")
        print("3 - Exibir tarefas")
        print("4 - Sair")
        print("+-----------------------------------+")

        opcao = int(input("Digite uma opção: "))

        if (opcao == 1):
            tarefa = input("Digite a tarefa:\n")
            tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso!")
        elif (opcao == 2):
            tarefa = input("Digite a tarefa a ser deletada: ")
            if tarefa in tarefas:
                tarefas.remove(tarefa)
                print("Tarefa deletada!")
            else:
                print("Tarefa não encontrada...")
        elif (opcao == 3):
            print("+----- LISTA DE TAREFAS -----+")
            for tarefa in tarefas:
                print("-", tarefa)
        elif (opcao == 4):
            print("SAINDO...")
            break
        else:
            print("Opção Inválida.")

GerenciadorTarefas()
