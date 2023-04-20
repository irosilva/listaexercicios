 # import math
print ('*'*50)
fabrica =float(input('digite o custo do carro :'))
print ('*'*50)

# processamento
distribuidora= (fabrica*28)/100
print (f'a percentagem da distribuidora é :{distribuidora:.2f}')
impostos = (fabrica*45)/100
print (f'o valor do imposto é:{impostos:.2f}')
valor_carro = distribuidora+impostos+fabrica 

print (f'o valor do carro é:{valor_carro:.2f}')