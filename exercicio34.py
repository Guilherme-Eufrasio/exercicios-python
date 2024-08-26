gen= input("Digite o seu gênero.\n EX H para Homem e M para Mulher\n: ")
altura= float(input("Digite sua altura: "))
altidealH= (72.7*altura)-57
altidealM= (62.1*altura)-44.7
if (gen== 'h' or gen=='H'):
  print(f"O seu peso ideal é de {altidealH}")
elif(gen=='m' or gen=='M'):
  print(f"O seu peso ideal é de {altidealM}")
else:
  print("Sexo inválido. Digite outro gênero.")