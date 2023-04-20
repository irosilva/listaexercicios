 # import math
print ('*'*50)
pequenas = int(input('digite a quantidade de camisetas pequenas : '))
medias = int(input('digite a quantidade de camisetas medias : '))
grandes = int(input('digite a quantidade de camisetas grandes : '))
print ('*'*50)
 
# processamento
precop =  pequenas*10
precom =  medias*12
precog =  grandes*15
compra =  precop + precom + precog

print (f'Pequenas: R$ {precop} Medias: R${precom} Grandes: R${precog}')
print (f'o valor da compra é : R$ {compra:.2f}')


print ('*'*50)

