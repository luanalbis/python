resposta = ''
soma = 0
contador = 0
lista = []
num =1 

while resposta != 'n':
	num = int(input('Digíte um número: '))
	soma = num + soma
	contador = contador + 1
	lista = lista + [num]
	
	resposta = input('Deseja continuar(S/N)? ').lower()
	print(' ')

print('A soma é: {}'.format(soma))	
print('A média é: {}'.format(soma/contador))
print ('O maior é {} e o menor é {}'.format(max(lista),min(lista)))