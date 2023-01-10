def idade():
	while True:
		try:
			age = float(input('Qual sua idade? '))
			if age < 0:
				print('Digite um numero valido!\n')
				continue			
			return (f'{age*365:.0f}')	
			
		except ValueError:
			print('Digite um numero válido!\n ')
			continue			
print(idade())

	

	