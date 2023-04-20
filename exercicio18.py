 # import math
print ('*'*50)
salario = float (input('digite o seu salário : '))

print ('*'*50)
 
# processamento
aumento = (salario*15)/100
salarioaumentado = (salario + aumento)
imposto = (salarioaumentado*8)/100
salario_atual= (salarioaumentado-imposto)

print (f'O salário inicial é de: R$ {salario}')
print (f'O salário com aumento de 15% é de : R$ {salarioaumentado}')
print (f'O salário Final é de: R$ {salario_atual}')


print ('*'*50)

