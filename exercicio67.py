tabe = []
t = 0
ta = 0
b = 0
ti = 0
v = []
pontos = []
e = []
d = []
golf = []
gt = []
saldo = []
for ti in range(t,4):
  tabela = tuple()
  time = input(f"Digite o {ti+1}º time: ")
  p = 0
  for ta in time:
    v = int(input("Digite a quantidade de vitórias: "))
    d = int(input("Digite a quantidade de derrotas: "))
    e = int(input("Digite a quantidade de empates: "))
    golf = int(input("Digite a quantidade de gols feitos: "))
    gt = int(input("Digite a quantidade de gols tomados: "))
    pontos = v*3
    e = e
    pontos=+e
    saldo = golf-gt
    break
  tabela = time, pontos, v, e, d, golf, gt, saldo
  tabe.append(tabela)
  ta =+1
  print("+------------------------------------+")
  print("|Time | P | V | E | D | GP | GC | SG |")
  print("+------------------------------------+")
for b in range (b,4):
  print(f"| {tabe[b][0]} | {tabe[b][1]} | {tabe[b][2]} | {tabe[b][3]} | {tabe[b][4]} | {tabe[b][5]} | {tabe[b][6]} | {tabe[b][7]} |")
  print("+------------------------------------+")
  b =+1