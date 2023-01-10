from random import choice

numero = [1,2,3,4,5,6,7,8,9,10]
meu = 0
tentativas = 0
robo = 1
while meu != robo:
	meu = int(input('Digíte seu número: '))
	robo = choice(numero)
	print ('Numero do npc: ',robo)
	print (' ')
	tentativas = tentativas + 1
	

print(' ')
print('Número de tentativas {}'.format(tentativas))
	

