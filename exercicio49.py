n1=1
n2=1
n3=0
i=3
posi=int(input("Informe uma posição da sequencia de Fibonacci que deseja saber: "))
while i<=posi:
  n3=n1+n2
  n1=n2
  n2=n3
  i=i+1

print (n3)