from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
cont = 1
print('Valores sorteados!')
while True:
	for c in range (1,5):
		sleep(0.3)
		num = randint(1,6)
		jogo[c] = num
		print(f'   O player{c} tirou {num} no dado')
	
	print('\nRanking geral: ')
	rank = {}
	rank = sorted(jogo.items(),key= itemgetter(1),reverse=True)
	
	for k,v in rank:
		sleep(0.3)
		print('   {}° Lugar player{},tirou {}'.format(cont,k,v))
		cont+=1
	resp = input('\nContinuar?')
	print()
	cont = 1
	
	if resp == 'n':
		break
	