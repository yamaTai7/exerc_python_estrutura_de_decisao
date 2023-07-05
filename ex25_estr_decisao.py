# Q25 https://wiki.python.org.br/EstruturaDeDecisao
# investigação
q1=input("Vc Telefonou para a vítima?(sim ou não): ")
q2=input("Vc Esteve no local do crime?(sim ou não): ")
q3=input("Vc Mora perto da vítima?(sim ou não): ")
q4=input("Vc Devia para a vítima?(sim ou não): ")
q5=input("Vc Já trabalhou com a vítima?(sim ou não): ")

for i in range(0,5):
    tsim=0
    if q1=='sim':
       tsim+=1
   
    if q2=='sim':
       tsim+=1
    
    if q3=='sim':
       tsim+=1
    
    if q4=='sim':
       tsim+=1
    
    if q5=='sim':
       tsim+=1
#print(tsim) 
        
if tsim == 2:
        print('VC é suspeito!\n')
        exit()
         
if tsim>=3 and tsim<=4:
        print('VC é cúmplice!\n')
        exit()
         
if tsim==5:
       print('VC É O ASSASSINNO!\n')
       exit()
         
else:
      print('VC é inocente!\n')
         