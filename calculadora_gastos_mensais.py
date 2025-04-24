receitas = []
despesas = {"Moradia": 0, "Alimentação": 0, "Transporte": 0, "Lazer": 0, "Saúde": 0, "Educação": 0, "Comunicação": 0, "Impostos": 0, "Outros": 0}

def adicionar_receita(valor):
  receitas.append(valor)
  print(f"Receita de R$ {valor:.2f} adicionada com sucesso!")

def adicionar_despesa(categoria, valor):
  if categoria in despesas:
    despesas[categoria] += valor
    print(f"Despesa de R$ {valor:.2f} adicionada na categoria '{categoria}' com sucesso!")
  else:
    print(f"Categoria '{categoria}' não encontrada!")

def exibir_resumo():
  total_receitas = sum(receitas)
  total_despesas = sum(despesas.values())
  saldo = total_receitas - total_despesas

  print("\nResumo financeiro:")
  print(f"Total de receitas: R$ {total_receitas:.2f}")
  print(f"Total de despesas: R$ {total_despesas:.2f}")
  print(f"Saldo: R$ {saldo:.2f}")
  print("\nDespesas por categoria:")
  for categoria, valor in despesas.items():
    print(f"{categoria}: R$ {valor:.2f}")

def salvar_dados():
  with open("dados_financeiros.txt", "w") as arquivo:
    arquivo.write("Receitas:\n")
    for receita in receitas:
      arquivo.write(f"{receita:.2f}\n")
      arquivo.write("Despesas:\n")
      for categoria, valor in despesas.items():
        arquivo.write(f"{categoria}: {valor:.2f}\n")
      print("Dados financeiros salvos com sucesso!")

def carregar_dados(arquivo):
  try:
    with open("dados_financeiros.txt", "r"): 
      linhas = arquivo.readlines()
      receitas.clear()
      despesas.clear()
      for linha in linhas:
        if linha.startswith("Receita:"):
          receitas = [float(valor) for valor in linha.split(":") if valor.strip()]
        elif linha.startswith("Despesa:"):
          categoria, valor = valor.split(":")
          categoria = categoria.strip()
          valor = float(valor.strip())
          if categoria in despesas:
            despesas[categoria] = valor
          else:
            despesas[categoria] = valor
      print("Dados financeiros carregados com sucesso!")
  except FileNotFoundError:
    print("Arquivo de dados financeiros não encontrado. Nenhum dado foi carregado.")
  except Exception as e:
    print(f"Erro ao carregar dados financeiros: {e}")

def sair():
  print("\nAté a próxima!")
  exit()

