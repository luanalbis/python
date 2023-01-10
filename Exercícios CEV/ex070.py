resposta = 's'
produto = 0.0
contador = 0
barato = ' '
maisbarato = 0


while resposta != 'n':

	nome = input('Nome do produto: ')
	preco = float(input('Valor do produto:R$'))
	produto = produto + preco
	print (' ')
	
	resposta = input('Continuar: [S/N]').lower()
	print(' ')
	while resposta != 's' and resposta != 'n':
		resposta = input('Continuar: [S/N]').lower()
		
	if preco > 1000:
		contador = contador + 1
	
	if preco > 0:
		maisbarato= preco
		barato = nome
	if preco < maisbarato:
		barato = nome
		maisbarato = preco
		
print(' ')			
print (f'Valor total dos produtos: R${produto:.2f}')
print (f'Total de produtos que passaram dos R$1000: {contador}')
print(f'Produto mais barato {barato}, R${maisbarato:2f}')
