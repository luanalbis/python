resposta = [1,2,3,4,5]
escolha = 0
resultado = 0

while escolha != 5:
	num1 = int(input('Digíte um número: '))
	num2 = int(input('Digíte um número: '))
	print (' ')
	print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair\n')
	escolha = int(input('Escolha uma opção:' ))
	
	if escolha == 1:
		resultado = num1 + num2
		print('Resultado:',resultado)
		print (' ')
	
	if escolha == 2:
		resultado = num1 * num2
		print('Resultado:',resultado)
		print(' ')
	
	if escolha == 3:
		if num1 > num2:
			print(f'{num1} é maior que {num2}')
			print(' ')
		if num2 > num1:
			print(f'{num2} é maior que {num1}')
			print(' ')
		if num1 == num2:
			print('Números iguais!')
			print(' ')
			
	if escolha == 4:
		print('Escolha novamente!!')
		print(' ')
	
	
			
		