valor = int(input("Insira um valor para saber se é primo ou não: "))

# Verifica se o número é menor que 2, pois números menores que 2 não são primos
if valor < 2:
    print("\nO valor não é primo")
else:
    # Inicializa uma variável para verificar se o número é primo
    eh_primo = True
    
    # Verifica divisores de 2 até a raiz quadrada do valor
    for i in range(2, int(valor**0.5) + 1):
        if valor % i == 0:  # Se o valor é divisível por i
            eh_primo = False  # Não é primo
            break  # Não precisa continuar verificando

    # Exibe o resultado com base na verificação
    if eh_primo:
        print("\nO valor é primo")
    else:
        print("\nO valor não é primo")