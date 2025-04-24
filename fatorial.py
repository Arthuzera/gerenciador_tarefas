# Inicializa a variável resultado com 1, que será usada para armazenar o fatorial
resultado = 1

# Solicita ao usuário que insira um número inteiro e converte a entrada para um inteiro
valor = int(input("\nInsira um número para ter sua fatorial gerada: "))

# Verifica se o número inserido é negativo
if valor < 0:
    # Se o número for negativo, exibe uma mensagem de erro
    print("Por favor, não inserir um número negativo!")
else:
    # Se o número for não negativo, inicia o cálculo do fatorial
    # O loop irá iterar de 1 até o valor inserido (inclusive)
    for i in range(1, valor + 1):
        # Multiplica o resultado atual pelo número atual do loop (i)
        resultado = resultado * i

# Após o loop, exibe o resultado final do fatorial
print(f"\nO fatorial de {valor} é: {resultado}")