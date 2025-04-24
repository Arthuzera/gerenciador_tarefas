lista_compras = []

while True:
    print("\nMenu:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Ver lista de compras")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == '1':
        item = input("Digite o nome do item a ser adicionado: ")
        lista_compras.append(item)
        print(f"'{item}' foi adicionado à lista de compras.")
    
    elif opcao == '2':
        item = input("Digite o nome do item a ser removido: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"'{item}' foi removido da lista de compras.")
        else:
            print(f"'{item}' não está na lista de compras.")
    
    elif opcao == '3':
        print("Lista de Compras:")
        if lista_compras:
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")
        else:
            print("A lista de compras está vazia.")
    
    elif opcao == '4':
        print("Saindo do programa. Até logo!")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")