from random import randint as r
import math

print ('Um momento, irei pensar em um número de 0 à 5 :)')
print(' ')

resp = int(input('Tente advinhar o número que eu pensei: '))

num = int(r(0,5))

print (f'Número que pensei:{num}')
print(' ')

if resp == num:
	
	print ('Parabéns, voçê advinhou!:)')
else:
	
	print ('Você errou, tente outra vez :(')

