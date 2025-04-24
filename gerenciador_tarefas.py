tarefas = {}

def adicionar_tarefa(tarefa):
    tarefas[tarefa] = False
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def visualizar_tarefas():
    if tarefas:
        print("Lista de tarefas:")
        for tarefa, concluida in tarefas.items():
            status = "Concluída" if concluida else "Pendente"
            print(f"Tarefa: {tarefa}, Status: {status}")
    else:
        print("Nenhuma tarefa cadastrada.")

def marcar_tarefa_concluida(tarefa):
    if tarefa in tarefas:
        tarefas[tarefa] = True
        print(f"Tarefa '{tarefa}' marcada como concluída!")
    else:
        print(f"Tarefa '{tarefa}' não encontrada!")

def remover_tarefa(tarefa):
    if tarefa in tarefas:
        del tarefas[tarefa]
        print(f"Tarefa '{tarefa}' removida da lista!")
    else:
        print(f"Tarefa '{tarefa}' não encontrada!")

def sair():
    print("\nAté a próxima!")
    exit()

while True:
    print("\nMenu:")
    print("1- Adicionar tarefa")
    print("2- Visualizar tarefas")
    print("3- Marcar tarefa como concluída")
    print("4- Remover tarefa")
    print("5- Sair")

    opcao = input("\nSelecione uma opção(1-5): ")

    if opcao == "1":
        tarefa = input("\nAdicione a tarefa: ")
        adicionar_tarefa(tarefa)
    
    elif opcao == "2":
        visualizar_tarefas()

    elif opcao == "3":
        tarefa = input("\nDigite o nome da tarefa a ser marcada como concluída: ")
        marcar_tarefa_concluida(tarefa)

    elif opcao == "4":
        tarefa = input("\nDigite o nome da tarefa a ser removida: ")
        remover_tarefa(tarefa)

    elif opcao == "5":
        sair()

    else:
        print("\nOpção não reconhecida, tente novamente!")