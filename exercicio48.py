qtde_par = 0
qtde_imp = 0
for i in range(10):
  num = int(input(f"Digite o {i+1}° número: "))
  if (num % 2 == 0):
    qtde_par += 1
  else:
    qtde_imp += 1

print(f"A quantidade de números pares é de {qtde_par}")
print(f"A quantidade de números ímpares é de {qtde_imp}")