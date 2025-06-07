import random

def main():
  print("Lista de Chamada\n")
  i = int(input("Digite a quantidade de alunos:  "))
  vet = [""] * i
  j = 0

  for i in vet:
    vet[j] =input("digite o nome do aluno:  ")
    j = j + 1
  nome = "Lauane Gomes de Moraes"
  
  print("As cinco primeiras letras do seu nome são: ", nome[0:6])
  print("Alunos que vieram hoje ", vet)
  
  return 0
main()