num1= int(input("Digite um número a ser fatorado: "))
c=num1
while c>1:
  num2=num1*(c-1)
  num1=num2
  c=c-1
print(f"O valor fatorado foi de {num2}")