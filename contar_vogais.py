def contar_vogais(frase):
  return len(frase.replace(" ", ""))

while True:
  frase = input("\nDigite uma frase (ou 'sair' para encerrar): ")

  if frase.lower() == 'sair':
    print("\nPrograma encerrado, até depois!")
    break

  num_vogais = contar_vogais(frase)

  print(f"\nA quantidade de palavras nessa frase é de: {num_vogais}")