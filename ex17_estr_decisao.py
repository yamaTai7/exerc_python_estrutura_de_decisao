# Q17_https://wiki.python.org.br/EstruturaDeDecisao
# ano bissexto
  
a=float(input('Informe algum ano: '))
if a==0:
    print('\nTente outra vez!\n')
    exit()
if a<0:
    print('\nTente outra vez!\n')
    exit()
    

if (a%4==0 and a%100!=0) or (a%400==0):
    print('Este ano é bissexto!\n')
    
else:
    print('Este ano não é bissexto!\n')
    
