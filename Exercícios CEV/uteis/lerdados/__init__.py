def leiaint(a):
	while True:
		try:
			n = int(input(a))
		except(ValueError,TypeError):
			print('ERRO, Digíte um numero válido!')
			continue
			
		except KeyboardInterrupt:
			print('Número não digitado!')
			return 0
			
		else:
			print('Valor adcionado!')
			return n
		
		
def leiafloat(a):
	while True:
		try:
			f = float(input(a))
		except (ValueError,TypeError):
			print('ERRO, Digíte um numero válido!')
			continue
		except KeyboardInterrupt:
			print('Número não digitado!')
			return 0
			
		else:
			print('Valor adcionado')
			return f