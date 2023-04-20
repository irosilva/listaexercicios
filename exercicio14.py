 # import math
print ('*'*50)
paes = int(input('digite a quantidade de paes vendidas no dia : '))
bolos = int(input('digite a quantidade de bolos vendidos no dia : '))
print ('*'*50)
 
# processamento
paes_dia = paes*0.12
bolos_dia = bolos*1.50
soma= paes_dia+bolos_dia
poupanca= (soma*10)/100

print (f'o ganho total do dia é :{soma}')
print (f'o valor que deve ser colocado na poupança é :{poupanca:.2f}')

print ('*'*50)

