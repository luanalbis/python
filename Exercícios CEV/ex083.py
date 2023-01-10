exp = (input('Digíte uma expressão matemática: '))

p1 = exp.count('(')
p2 = exp.count (')')


if p1 + p2 == 0:
	print('Sua expressão esta correta!')
	
if p1 == p2 > 0:
		print('Sua expressão esta correta!')

elif p1 > 0 or p2 >0:
		print('Sua expressão está incorreta !')
	



