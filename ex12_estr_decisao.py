# Q12https://wiki.python.org.br/EstruturaDeDecisao
# contra-cheque
ent1= float(input('Entre o valor da sua hora trabahada:  '))
ent2= float(input('Entre as horas trabalhadas/mês: '))
sl=ent1*ent2
slr=round(sl,2)
print('Salário bruto neste mês é de R$',slr,'\n')
if sl <= 900.00:
    print('**Seu salário é isento de Imp. de Renda**')
    fgts=sl*0.11
    fgtsr=round(fgts,2)
    inss=sl*0.10
    inssr=round(inss,2)
    sind=sl*0.03
    sindr=round(sind,2)
    slq=sl-(fgtsr+inssr+sindr)
    slqr=round(slq,2)
    print('\nSeu salário Bruto é ',slr)
    print('Desconto de FGTS(11%) R$',fgtsr)
    print('Desconto de INSS(10%) R$',inssr)
    print('Desconto de SINDICATO(3%) R$',sindr)
    print('Seu salário líquido R$', slqr,'\n')
    exit()
if sl>900 and sl<= 1500:
    desc='5%'
    ir=sl*0.05
    irr=round(ir,2)
if sl>1500 and sl<=2500.00:
    desc="10%"
    ir=sl*0.10
    irr=round(ir,2)
if sl>2500:
    desc="20%"
    ir=sl*0.20
    irr=round(ir,2)
    
fgts=sl*0.11
fgtsr=round(fgts,2)
inss=sl*0.10
inssr=round(inss,2)
sind=sl*0.03
sindr=round(sind,2)
slq=float(sl-(irr+fgtsr+inssr+sindr))
slqr=round(slq,2)
print('Seu salário Bruto é ',slr)
print('Desconto de IR (',desc,')',irr)
print('Desconto de FGTS(11%) R$',fgtsr)
print('Desconto de INSS(10%) R$',inssr)
print('Desconto de SINDICATO(3%) R$',sindr)
print('Seu salário líquido R$', slqr)



