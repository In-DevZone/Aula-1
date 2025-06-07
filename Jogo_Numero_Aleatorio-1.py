import random

def main():
  print("Bem vindo ao jogo de adivinhação!")
  numAleatorio = random.randint(1, 200)

  tentativas = 0
  numDigitado = 0

  while numDigitado != numAleatorio:
    numDigitado = int(input("Digite um numero:  "))

    if numDigitado == numAleatorio:
      print("Voce acertou!\n")
    elif numDigitado < numAleatorio: 
      print("O numero digitado é menor que o numero aleatorio\n")
    else:
      print("O numero digitado é maior que o numero aleatorio\n")
    tentativas += 1

  print("Voce acertou em", tentativas, "tentativas")

  return 0
main()