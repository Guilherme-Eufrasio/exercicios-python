turno= input("Digite seu período escolar.\n M para Matutino, V para Vespertino e N para Noturno\n") [0]
if(turno=='M' or turno=='m'):
  print("Bom Dia")
elif(turno=='V' or turno=='v'):
  print ("Boa Tarde")
elif (turno=='N' or turno=='n'):
  print("Boa noite")
else:
  print("Período Inválido. Digite outro período")
  
