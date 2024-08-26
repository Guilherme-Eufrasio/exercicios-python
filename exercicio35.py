import math
area= float(input("Informe a área a ser pintada em metros quadrados: "))
tinta=18
preco=80
qtde_lata= math.ceil(float(area/tinta))
precoT= qtde_lata*preco
print((qtde_lata))
print (f"A quantidade de latas para pinta esses metros quadrados vai ser de {qtde_lata} latas e o preço total vai ser de {precoT} reais")