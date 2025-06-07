def main():
  idade = int(input("Informe sua idade:  "))

  if idade >= 18:
   print("Entrada Liberada!")
  elif idade >= 16:
    acompanhante = input("Possui acompanhante? (S/N)")
    if acompanhante == "s" or acompanhante == "S":
     print("Entrada Liberada!")
    else: 
      print("Entrada Proibida!")
  else:
   print("Entrada Proibida!")
    
  return 0
main()