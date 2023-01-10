from random import  choice
r = input('Pedra, Papel ou Tesoura?: ').lower().strip()

lista = ['pedra','papel','tesoura']
com = choice(lista)
print('Sua escolha:{}'.format(r))
print('Minha escolha:{}'.format(com))

if r == 'tesoura' and com == 'papel' or r == 'papel' and com == 'pedra' or r == 'pedra' and com == 'tesoura':
	print ('VOÇÊ GANHOU!')

elif r == com:
	print('EMPATAMOS')
else:
	print('VOCÊ PERDEU!')
	