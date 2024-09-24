
porc=0
prec=0
desc=0
valor=0
print("a para Álcool\n")
print("g para Gasolina\n")
tipoc=(input("Tipo do Combustivel: ").lower())
l=float(input("Digite a quantidade de litros: "))
if (tipoc=='a'):
  if(l<=20):
    porc=l*3
    prec=l*3.90
    desc=(prec*porc)/100
    valor=desc-prec
  else:
    porc=l*5
    prec=l*3.90
    desc=(prec*porc)/100
    valor=desc-prec
elif(tipoc=='g'):
  if(l<=20):
    porc=l*5
    prec=l*5.50
    desc=(prec*porc)/100
    valor=desc-prec
  else:
    porc=l*6
    prec=l*5.50
    desc=(prec*porc)/100
    valor=desc-prec
else:
  print("Tipo de combustivel errado")
print(f"Irá pagar R$ {valor}")