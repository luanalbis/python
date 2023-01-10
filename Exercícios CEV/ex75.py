import math
lista = (int(input('Número: ')),int(input('Número: ')),int(input('Número: ')),int(input('Número: ')))
print(' ')
print('Números {}'.format(lista))

print('Número 9 apareceu {} vezes'.format(lista.count(9)))

if 3 not in lista:
	print('Número 3 não foi escontrado')	
else:
	print('Número 3 apareceu primeiro na posicão {}'.format(lista.index(3)+1))

print ('Números pares:',end=(' '))
for n in lista:
	if n % 2 ==0:
		print (n , end=(' '))

