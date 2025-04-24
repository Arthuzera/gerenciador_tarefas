def contar_palavras(frase):
  palavras = frase.split()
  return len(palavras)

def contar_caracteres(frase):
  return len(frase.replace(" ", ""))

def palavra_mais_longa(frase):
  palavras = frase.split()
  if palavras:
    return max(palavras, key=len)
  return ""

while True:
  frase = input("\nDigite uma frase (ou 'sair' para encerrar): ")

  if frase.lower() == 'sair':
    print("\nPrograma encerrado, até depois!")
    break

  num_palavras = contar_palavras(frase)
  num_caracteres = contar_caracteres(frase)
  maior_palavra = palavra_mais_longa(frase)

  print(f"\nA quantidade de palavras nessa frase é de: {num_palavras}")
  print(f"\nA quantidade de caracteres nessa frase é de (sem espaços): {num_caracteres}")
  print(f"\nA maior palavra nessa frase é: {maior_palavra}")