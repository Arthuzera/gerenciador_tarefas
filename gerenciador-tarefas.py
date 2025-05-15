"""
Gerenciador de Tarefas - Versão melhorada
- Estruturação básica do código
- Funções com responsabilidades bem definidas
- Persistência básica de dados
- Validações simples
"""
import os
import json

# Constantes
ARQUIVO_TAREFA = 'tarefas.json'

def carregar_tarefas():
    """Carregar as tarefas salvas do arquivo, caso existir."""
    if os.path.exists(ARQUIVO_TAREFA): # Verificar se o arquivo das tarefas exista
        try:
            with open(ARQUIVO_TAREFA, 'r', encoding='utf-8') as arquivo: # Abrindo o arquivo 'tarefas.json' de forma segura
                return json.load(arquivo) # Processar os dados dentro do arquivo
        except json.JSONDecodeError:
            print('Erro ao carregar o arquivo de tarefas. Criando nova lista.')
            return {} # Caso aconteça algum tipo de erro ao carregar o arquivo, criar um novo arquivo vazio
    return {} # Caso o arquivo não exista, criar um arquivo json, vazio claro

def salvar_tarefas(tarefas):
    """Salvar as tarefas em um arquivo JSON."""
    with open(ARQUIVO_TAREFA, 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4) # Serialiazar/Adicionar as 'tarefas' no 'arquivo'

def adicionar_tarefa(tarefas, tarefa):
    """Adicionar uma tarefa a lista."""
    if not tarefa.strip(): # Validação simples para saber se foi adicionada alguma tarfera
        print('Erro: A tarefa não pode estar vazia!')
        return
    
    if tarefa in tarefas: # Verificar se a tarefa já existe
        print(f'Aviso: A tarefa {tarefa} já existe!')
        return
    
    tarefas[tarefa] = False
    salvar_tarefas(tarefas) # Chamar a função para salvar a tarefa no arquivo
    print(f"Tarefa '{tarefa}' foi adicionada com sucesso!")

def visualizar_tarefas(tarefas):
    """Exibir todas as tarefas cadastradas."""
    if tarefas: # Verificar se existem tarefas cadastradas
        print('\nListas de tarefas:')
        print('-'*40)
        for i, (tarefa, concluida) in enumerate(tarefas.item(), 1):
            status = "Concluida" if concluida else 'Pendente' # Verificar se a tarefa já foi concluída ou se ainda está pendente
            print(f"{i}. {tarefa:<30} - {status}.")
        print('-'*40)
    else:
        print('\nNenhuma tarefa cadastrada')

def marcar_tarefa_concluida(tarefas, tarefa):
    """Marcar uma tarefa como concluída."""
    if tarefa in tarefas: # Verifica se a tarefa existe na lista
        tarefas[tarefa]=True # Mudar o valor pra True, assinalando que ele foi concluida
        salvar_tarefas(tarefas)
        print(f"Tarefa '{tarefa}' marcada como concluída!")
    else:
        print(f"Tarefa '{tarefa}' não foi encontrada.")

def remover_tarefas(tarefas, tarefa):
    """Remover uma tarefa da lista."""
    if tarefa in tarefas: # Verificar se a tarefa está na lista
        del tarefas[tarefa] # Usar o del do python para eliminar de forma mais simples a tarefa da lista
        salvar_tarefas(tarefas) # Salvar a lista sem a tarefa que se deseja excluir
        print(f"Tarefa '{tarefa}' foi removida com sucesso!")
    else:
        print(f"Tarefa '{tarefa}' não foi encontrada na lista.")

def listar_e_selecionar_tarefa(tarefas, acao):
    """Exiba uma lista e permite seleciona algumas pelo seu número."""
    if not tarefas:
        return None
    
    lista_tarefas = list(tarefas.keys()) # Criar uma lista de tarefas usando suas chaves

    for i, tarefa in enumerate(lista_tarefas, 1):
        status = "Concluida" if tarefas[tarefa] else "Pendente"
        print(f" {i}. {tarefa} - {status}") # Enumerar os elementos dentro da lista de tarefas
    
    try:
        escolha = int(input("\nDigite o número da tarefa ou 0 para cancelar: ")) # Escolher o número da tarefa que quer visualizar individualmente
        if escolha==0:
            return None
        if 1 <= escolha <= len(lista_tarefas): # Verificar se o valor da escolha é válido, ou seja, a escolha deve ser um número entre 1 e a quantidade de elementos que temos dentro da lista
            return lista_tarefas[escolha - 1] # Retornar a tarefa escolhida. 'escolha - 1' porque as listas começam a contar de 0 em diante ou seja, se quisermos ver o primeiro elemento, séria 1-1=0 - 'lista_tarefas[0]' que é o primeiro elemento da lista.
        else:
            print("Número inválido!") # Verificação caso o número seja inválido, como um número negativo ou um número que não esteja entre 1 e o número total de tarefas dentro da lista.
            return None
    except ValueError:
        print("Entrada inválida! Digite um número.") # Exceção caso o valor digitado em escolha, não seja um número.
        return None    
    
def exibir_menu():
    """Exibe o menu de opções do programa."""
    print("\n" + "=" * 30)
    print("  GERENCIADOR DE TAREFAS")
    print("=" * 30)
    print("1- Adicionar tarefa")
    print("2- Visualizar tarefas")
    print("3- Marcar tarefa como concluída")
    print("4- Remover tarefa")
    print("5- Sair")
    print("=" * 30)


