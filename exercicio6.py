n1= int(input("Digite o 1° número: "))
n2= int(input("Digite o 2° número: "))
oprd = input("Digite um sinal para a conta: ")
if (oprd== '+'):
  resultado= n1+n2
  print (f"O resultado da conta foi {resultado}")
elif (oprd== '-'):
  resultado= n1-n2
  print(f"O resultado da conta foi de {resultado}")
else:
  print("Operação inválida. Digite o sinal de + ou -")