from exercicio51 import ehPrimo

if __name__ == '__main__':
  num = int(input("Digite um número: "))
  ehPrimo(num)
  p = num
  primos = []
  for p in range (2,num):
    if(ehPrimo(p)==True):
     primos.append(p)
    else:
      pass
  print (primos)
