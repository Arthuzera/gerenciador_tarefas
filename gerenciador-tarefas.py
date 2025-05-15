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
    
    if tarefa in tarefas:
        print(f'Aviso: A tarefa {tarefa} já existe!')
        return
    
    tarefas[tarefa] = False
    salvar_tarefas(tarefas)
    print(f"Tarefa '{tarefa}' foi adicionada com sucesso!")
