contatos = {}

def adicionar_contato(nome, telefone):
  contatos[nome] = telefone
  print(f"Contato '{nome}' adicionado com sucesso!")

def visualizar_contato():
  if contatos:
    print("Lista de contatos")
    for nome, telefone in contatos.items():
      print(f"Contato: {nome}, Telefone: {telefone}")

def buscar_contato(nome):
  if nome in contatos:
    print(f"Contato encontrado: Nome: {nome}, Telefone: {contatos[nome]}")
  else:
    ("Contato '{nome}' não encontrado!")

def remover_contato(nome):
  if nome in contatos:
    del contatos[nome]
    print(f"Contato '{nome}' removido da lista!")
  else:
    (f"Contato '{nome}' não encontrado!")

while True:
  print("\nMenu:")
  print("1- Adicionar contato")
  print("2- Visualizar contatos")
  print("3- Buscar contato")
  print("4- Remover contato")
  print("5- Sair")

  opcao = input("Selecione uma opção(1-5): ")

  if opcao == "1":
    nome = input("Adicione o contato: ")
    telefone = input("Adicione o telefone: ")
    adicionar_contato(nome, telefone)
  
  elif opcao == "2":
    visualizar_contato()

  elif opcao == "3":
    nome = input("Digite o nome do contato a ser buscado: ")
    buscar_contato(nome)

  elif opcao == "4":
    nome = input("Digite o nome do contato a ser removido: ")
    remover_contato(nome)

  elif opcao == "5":
    print("\nAté a próxima")
    break

  else:
    print("\nOpção não reconhecida, tente novamente!")