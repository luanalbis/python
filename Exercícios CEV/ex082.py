resposta = ' '
lista = []
par = []
impar = []
while resposta != 'n':
	num = int(input('Número: '))
	lista.append(num)
	if num % 2 == 0:
		par.append(num)
	else:
		impar.append(num)
	resposta = input('Continuar?S/N: ').lower().strip()[0]
	while resposta not in 'sn':
			resposta = input('Erro.Continuar?S/N: ').lower().strip()[0]

print('\nLista de numeros:\n{}'.format(lista))
print(' ')
print('Números pares: \n{}'.format(par))
print(' ')
print('Números impares: \n{}'.format(impar))