from random import randint
from time import sleep
cont = 0
lista =[]

while True:
	resp = input('Iniciar sorteio?[S/N]').lower().strip()[0]
	
	while resp not in 'sn':
		resp = input('\nIniciar sorteio?[S/N]').lower().strip()[0]
	if resp == 'n':
		print(' ')
		print('OBRIGADO POR PARTICIPAR')
		break
		
	if resp == 's':
		print(' ')	
		for c in range (1,10):	
			for p in range(0,1):
				while cont < 6:
					num = randint(1,60)
					lista.append(num)
					if lista.count(num) >1:
						lista.remove(num)
						cont -=1
									
					cont = cont+1
				sleep(0.5)
				print('{}° SORTEIO - {}'.format(c,sorted(lista)))			
			cont = cont-6
			lista.clear()		
					
		print(' ')			
			
			