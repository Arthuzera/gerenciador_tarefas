# Gerenciador de Tarefas

Um aplicativo simples de linha de comando para gerenciar suas tarefas diárias.

## Funcionalidades

- Adicionar novas tarefas
- Visualizar todas as tarefas cadastradas
- Marcar tarefas como concluídas
- Remover tarefas
- Persistência de dados (as tarefas são salvas entre execuções)

## Como usar

1. Execute o programa:
   ```
   python gerenciador_tarefas_melhorado.py
   ```

2. Use o menu para navegar:
   - **Opção 1**: Adicionar uma nova tarefa
   - **Opção 2**: Visualizar todas as tarefas
   - **Opção 3**: Marcar uma tarefa como concluída
   - **Opção 4**: Remover uma tarefa
   - **Opção 5**: Sair do programa

3. As tarefas são salvas automaticamente em um arquivo `tarefas.json`

## Exemplo de uso

```
==============================
  GERENCIADOR DE TAREFAS
==============================
1- Adicionar tarefa
2- Visualizar tarefas
3- Marcar tarefa como concluída
4- Remover tarefa
5- Sair
==============================

Selecione uma opção (1-5): 1

Adicione a tarefa: Estudar Python
Tarefa 'Estudar Python' adicionada com sucesso!

Selecione uma opção (1-5): 2

Lista de tarefas:
----------------------------------------
1. Estudar Python                      ○ Pendente
----------------------------------------
```

## Estrutura do projeto

- **gerenciador_tarefas_melhorado.py**: O arquivo principal do programa
- **tarefas.json**: Arquivo de dados onde as tarefas são salvas

## Melhorias implementadas

Esta versão melhora o código original com:

1. **Persistência de dados**: As tarefas são salvas em um arquivo JSON
2. **Interface aprimorada**: Menu mais organizado e visual
3. **Seleção por número**: Opção de selecionar tarefas por número
4. **Validações**: Verificação de tarefas vazias e duplicadas
5. **Estrutura de código**: Funções com responsabilidades claras
6. **Tratamento de erros**: Para entradas inválidas

## Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa é necessária (apenas módulos da biblioteca padrão)

## Próximos passos

Futuras melhorias planejadas:

- Implementar classes para as tarefas
- Adicionar categorias ou tags
- Implementar prioridades
- Criar uma interface gráfica simples
