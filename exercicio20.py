 # import math
print ('*'*50)
moedas1Real= float (input('digite a quantidade de moedas de 1 Real : '))
moedas50= float (input('digite a quantidade de moedas de 0.50 Centavos : '))
moedas25= float (input('digite a quantidade de moedas de 0.25 centavos : '))
moedas10= float (input('digite a quantidade de moedas de 0.10 centavos : '))
moedas5= float (input('digite a quantidade de moedas de 0.05 centavos : '))
moedas1= float (input('digite a quantidade de moedas de 0.01 centavos : '))

print ('*'*50)
 
# processamento
total1real = (moedas1Real*1)
total50 = (moedas50*0.50)
total25 = (moedas25*0.25)
total10 = (moedas10*0.10)
total05 = (moedas5*0.05)
total01 = (moedas1*0.01)

valor_total = (total1real+total50+total25+total10+total05+total01)

print (f'O valor economizado é de : R$ {valor_total}')


print ('*'*50)

