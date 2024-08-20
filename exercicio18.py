vdep=float(input("Digite o valor do depósito: "))
txjuros=int(input("Digite a taxa de juros: "))
vlrend=(vdep*txjuros)/100
vlfinal=vdep+vlrend
print (f"O valor do rendimento foi de {vlrend}")
print (f"O valor total depois do depósito foi de {vlfinal} ")