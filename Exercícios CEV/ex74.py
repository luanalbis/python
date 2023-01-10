from random import randint
resposta = ' '
while resposta != 'n':
	a = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
	ordem = sorted(a)
	print('Números da tupla:',a)
	print(' ')
	print('Menor número:{}\n\nMaior Número:{}'.format(ordem[0],ordem[-1]))
	print(' ')
	resposta = input('Continuar com mais testes?(S/N)').lower().strip()[0]	
	while resposta not in ('sn'):
		resposta = input('Continuar com mais testes?(S/N)').lower().strip()[0]
	print(' ')
		
