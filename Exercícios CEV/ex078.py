lista = []
for c in range(1,6):
	num=int(input('Número: '))
	lista = lista + [num]
	
print('Posicao do maior numero: {} Maior numero: {}'.format(lista.index(max(lista))+1,max(lista)))
print('Posicao do menor numero: {} Menor numero: {}'.format(lista.index(min(lista))+1,min(lista)))