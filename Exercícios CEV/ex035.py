a = int(input ('Valor da primeira reta: '))
b = int(input ('Valor da segunda reta: '))
c = int(input ('Valor da terceira reta: '))

a1 = b + c
b1 = a + c
c1 = b + a

print(' ')

if  a1 > a:
	a1 = 1
	
if b1 > b:
	b1 = 1

if c1 > c:
	c1 = 1
	
if a1 + b1 + c1 == 3:
	print ('É possível formar um triângulo!')
	
else:
	print('Não é possível formar um triângulo!')
	
