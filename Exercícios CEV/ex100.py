from random import randint
from time import sleep

def sorteio():
		somapar =0
		print('Sorteando valores:',end=' ')
		for c in range(1,6):
			num = randint(1,10)
			numeros.append(num)
			print(num,end=' ',flush=True)
			sleep(0.5)
		for valor in numeros:	
			if valor %2 == 0:
				somapar += valor
		print ('Soma dos valores pares de {}. Temos {}'.format(sorted(numeros),somapar))
		
numeros = []		
sorteio()


