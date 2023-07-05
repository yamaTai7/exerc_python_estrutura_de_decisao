#Q8_https://wiki.python.org.br/EstruturaDeDecisao
#  menor PREÇO de três
n1=float(input('Entre o Preço 1 R$: '))
n2=float(input('Entre o Preço 2 R$: '))
n3=float(input('Entre o Preço 3 R$: '))
nMin = 1000000000000000000.0
if n1 < nMin:
      nMin=n1

if n2< n1:
     nMin=n2

if n3 < n2:
     nMin=n3
    
if n1==n2==n3:
    print('Tente outra vez.\n')
    exit()
     
print('O mais barato dos três é R$',nMin)


      

      
 

    





