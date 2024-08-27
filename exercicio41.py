n1= float(input("Digite o 1° número: "))
n2= float(input("Digite o 2° número: "))
n3= float(input("Digite o 3° número: "))
n4= float(input("Digite o 4° número: "))
n5= float(input("Digite o 5° número: "))
if (n1>n2 and n1>n3 and n1>n4 and n1>n5):
  print (f"O maior número é {n1}")
elif(n2>n1 and n2>n3 and n2>n4 and n2>n5):
  print (f"O mairo número é {n2}")
elif(n3>n1 and n3>n2 and n3>n4 and n3>n5):
  print(f"O maior número é {n3}")
elif(n4>n1 and n4>n2 and n4>n3 and n4>n5):
  print(f"O maior número é {n4}")
elif(n5>n1 and n5>n2 and n5>n3 and n5>n4):
  print (f"O maior número é {n5}")
else:
  print("O que você fez para aparecer essa mensagem??")