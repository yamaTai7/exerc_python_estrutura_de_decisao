# Q16_https://wiki.python.org.br/EstruturaDeDecisao
# equação do segundo grau
  
a=float(input('Informe o valor de A: '))
if a==0:
    print('\nNão será uma equação do segundo grau. Tente outra vez!\n')
    exit()
b=float(input('Informe o valor de B: '))
c=float(input('Informe o valor de C: '))
dlt=float(b**2 - 4*a*c)



if dlt<0:
    print('A equação não possui raizes reais.\n')
    exit()
if dlt==0:
    print('A  equação possui apenas uma raiz real.\n')
    exit()
if dlt>0:
    print('A  equação possui duas raízes reais.',dlt,'\n')
    exit()

    