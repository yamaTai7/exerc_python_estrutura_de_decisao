#Q11_https://wiki.python.org.br/EstruturaDeDecisao
#  reajuste salarial

n1=float(input('Informe seu salário R$: '))

if n1 <= 280.00:
      ac1=n1*0.2
      ac1r=round(ac1,2)
      reaj1=n1+ac1r
      reaj1r=round(reaj1,2)
      print('Vc recebeu um aumento de 20%.'
             'Um acréscimo de ',ac1r,
             'Seu salário será R$ ',reaj1r)
      
if n1 > 280.00 and n1 <=700.00:
      ac2=n1*0.15
      ac2r=round(ac2,2)
      reaj2=n1+ac2r
      reaj2r=round(reaj2,2)
      print('Vc recebeu um aumento de 15%.'
            'Um acréscimo de ',ac2r,
            'Seu salário será R$ ',reaj2r)
      
if n1 > 700.00 and n1 <=1500.00:
      ac3=n1*0.10
      ac3r=round(ac3,2)
      reaj3=n1+ac3r
      reaj3r=round(reaj3,2)
      print('Vc recebeu um aumento de 10%.'
            'Um acréscimo de ',ac3r,
            'Seu salário será R$ ',reaj3r)
      
if n1 >1500.00:
      ac4=n1*0.05
      ac4r=round(ac4,2)
      reaj4=n1+ac4r
      reaj4r=round(reaj4,2)
      print('Vc recebeu um aumento de 5%.'
             'Um acréscimo de ',ac4r,
             'Seu salário será R$ ',reaj4)


    
    
    


      

      
 

    





