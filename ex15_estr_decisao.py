# Q15https://wiki.python.org.br/EstruturaDeDecisao
# triângulos
    
l1=float(input('Informe o tamanho do lado: '))
l2=float(input('Informe o tamanho do lado: '))
l3=float(input('Informe o tamanho do lado: '))

if l1+l2>l3 or l3+l2>l1 or l1+l3>l2:
    print('\nOs tamanhos formam um triângulo.')
    
if l1==l2==l3:
    print('Um triângulo equilátero.\n')
    exit()
if l1==l2:
    print('Um triângulo isósceles.\n')
    exit()
if l1==l3:
    print('Um triângulo isósceles.\n')
    exit()
if l2==l3:
    print('Um triângulo isósceles.\n')
    exit()
if l1!=l2!=l3:
    print('Um triângulo escaleno.\n')
    exit()
    
    
    
    
