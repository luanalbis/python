resposta = ' '
lista = []

while resposta != 'n':
	num = int(input('Número: '))
	lista.append(num)
	
	resposta = input('\nContinuar?: ').strip().lower()[0]
	
	while resposta not in 'sn':
		resposta = input('\nTente novamente. Continuar?: ').lower()[0]

if 5 in lista:
	print('\nO número 5 apareceu {} vezes'.format(lista.count(5)))

else:
	print('\nNão foi encotrado número 5')
	
print('\nNumeros totais da lista: {}'.format(len(lista)))
print ('\nLista em ordem crescente:\n{}'.format(sorted(lista)))
print ('\nLista em ordem descrescente:\n{}'.format(sorted(lista,reverse=True)))
print()