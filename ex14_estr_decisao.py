# Q14https://wiki.python.org.br/EstruturaDeDecisao
# boletim

i=0
n=0
nota=0.0
soma=0.0
for i in range(0,2):
  nota=float(input('Entre a nota:'))
  if nota < 0.0 or nota >10.0:
     print('Nota inválida!\n')
     exit()
  if nota >= 0.0 and nota <=10.0:
     soma+=nota
     s=round(soma,2)
     m=s/2
     mr=round(m,2)
     n+=1
  
     if n==2:
         print('Total das notas = ',s)
         print('A média das notas é ',mr)
         
         if mr<=10 and mr>=9:
             con=('A')
             print('Seu conceito é ',con)
             print('Você está APROVADO!')
             
         if mr< 9 and mr>=7.5:
             con=('B')
             print('Seu conceito é ',con)
             print('Você está APROVADO!')
         if mr< 7.5 and mr>=6:
             con=('C')
             print('Seu conceito é ',con)
             print('Você está APROVADO!')
         if mr< 6 and mr>=4:
             con=('D')
             print('Seu conceito é ',con)
             print('Você está REPROVADO!')
         if mr< 4 and mr>=0:
             con=('E')
             print('Seu conceito é ',con)
             print('Você está REPROVADO!')
    