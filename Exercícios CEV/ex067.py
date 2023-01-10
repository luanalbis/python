num = 0

while num >= 0:
	num = int(input('Número: '))
	print ('-'*20)
	if num < 0:
		print('Programa de tabuada encerrado, volte sempre')
		break 
	
	if num >= 0:
		for c in range(1,11):
			print(f'{num} x {c} = {num*c}')
		
print(' ')	