n1=int(input("Digite o 1° número: "))
n2=int(input("Digite o 2° número: "))
n3=int(input("Digite o 3° número: "))
if(n1>n2 and n1>n3 and n2>n3):
  print(f"o maior número foi {n1}")
elif (n2>n1 and n2>n3 and n1>n3):
  print (f"O maior número foi {n2}")
elif (n3>n1 and n3>n2 and n1>n2):
  print(f"O maior número foi {n3}")
elif(n1>n2 and n1>n3 and n2>n3):
  print(f"O maior número foi {n1}")
elif (n2>n1 and n2>n3 and n3>n1):
  print (f"O maior número foi {n2}")
elif (n3>n2 and n3>n1 and n2>n1):
  print (f"O maior número foi {n3}")