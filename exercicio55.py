pala= input("Digite uma palavra: ")
palaRv= pala.lower().strip().replace(' ', '')
if (palaRv==palaRv[::-1]):
  print ("É um palindromo")
else:
  print ("Não é um palindromo")