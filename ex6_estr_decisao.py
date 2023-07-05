#Q6_https://wiki.python.org.br/EstruturaDeDecisao
# maior de três
n1=float(input('Entre o N1: '))
n2=float(input('Entre o N2: '))
n3=float(input('Entre o N3: '))
nMax = 0.0
if n1 > nMax:
      nMax=n1
      
if n2 > n1:
      nMax=n2
      
if n3 > n2:
     nMax=n3
    
if n1==n2==n3:
    print('Tente outra vez.\n')
    exit()
     
print('O maior número dos três é ',nMax)
 

    





