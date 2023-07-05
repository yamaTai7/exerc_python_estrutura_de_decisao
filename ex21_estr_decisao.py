# Q21 https://wiki.python.org.br/EstruturaDeDecisao
# CAIXA ELETRÔNICA
vl=float(input('Qual o valor do saque R$: '))

if vl<10 or vl>600:
    print('Valor proibido: Tente de R$ 10,00 a 600,00.')
if vl>=10 and vl<=600:
   cem=int(vl/100)
   vl=vl-(cem*100)
   cinq=int(vl/50)
   vl=vl-(cinq*50)
   dez=int(vl/10)
   vl=vl-(dez*10)
   cinc=int(vl/5)
   vl=vl-(cinc*5)
   um=int(vl/1)
   if cem==0 and cinq!=0:
       print('Notas de 50:',cinq)
       print('Notas de 10:',dez)
       print('Notas de 5:',cinc)
       print('Notas de 1:',um,'\n')
       exit()
   if cem==0 and cinq ==0:
       print('Notas de 10:',dez)
       print('Notas de 5:',cinc)
       print('Notas de 1:',um,'\n')
       exit()
   else:
       print('Notas de 100: ',cem)
       print('Notas de 50:',cinq)
       print('Notas de 10:',dez)
       print('Notas de 5:',cinc)
       print('Notas de 1:',um)
       
    