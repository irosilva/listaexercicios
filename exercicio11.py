 # import math
print ('*'*50)

valordepositado = float(input('digite o valor que vai ser depositado: R$ '))

print ('*'*50)
 
# processamento
juros = (valordepositado*0.70)/100
       
valor_atual = valordepositado+juros


print (f'O valor do juros é:R${juros:.2f} e o valor atual é: R${valor_atual:.2f}')


