n1= int(input("Digite a 1° nota: "))
n2= int(input("Digite a 2° nota: "))
n3= int(input("Digite a 3° nota: "))
n4= int(input("Digite a 4° nota: "))
materia= input("Digite o nome da matéria: ")
media = (n1+n2+n3+n4)/4
if (media>=7):
       print (f"Você foi aprovado em {materia} com a nota média de {media}")
elif (media>=5): 
        print(f"Você esta de recuperação na matéria de {materia} com a nota média de {media}")
else:
        print(f"Você foi reprovado em {materia} com a nota média de {media}")