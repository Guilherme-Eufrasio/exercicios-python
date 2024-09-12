primo=False
num= int(input ("Digite um número: "))
if(not(num%2==0)or num==2):
  primo=True
  for n in range (3,num):
    if(num%n==0):
      primo=False
      break 
if (primo):
  print(f"O número é primo")
else:
  print(f"O número não é primo")
  