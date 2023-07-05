#Q9_https://wiki.python.org.br/EstruturaDeDecisao
#  ordem decrescente

n1=int(input('Entre o número 1: '))
n2=int(input('Entre o número 2: '))
n3=int(input('Entre o número 3: '))
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
     
     
if n1>n2>nMin:
    print(n1,n2,nMin)
if n2>n1>nMin:
    print(n2,n1,nMin)
if n3>n2>nMin:
    print(n3,n2,nMin)
if n2>n3>nMin:
    print(n2,n3,nMin)
if n3>n1>nMin:
    print(n3,n1,nMin)
if n1>n3>nMin:
    print(n1,n3,nMin)
    
    
    


      

      
 

    





