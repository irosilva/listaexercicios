 # import math
print ('*'*50)

vendedor= input('digite o nome do vendedor(a) : ')
salario_fixo = float(input('digite o salario fixo : '))
vendas = float(input('digite o valor total das vendas mensais : '))
comissao= 15
print ('*'*50)
 
# processamento
salario_atual=((vendas*comissao)/100)+salario_fixo


print (f'O vendedor: {vendedor} ganha R${salario_fixo:.2f} e com a comissão recebeu:R${salario_atual:.2f}')


