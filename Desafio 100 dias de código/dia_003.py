def grill():
	from random import randint
	geral = contx = conto = 0
	list_churras = []
	while geral < 3:
		cont   = 0
		numeros = []
		pedido = ' '
		churrasco = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-',]
		pedido = input('Churrasco: ').upper().strip()
		while True:
			print()
			if pedido.count('O') + pedido.count('X') == 6 and len(pedido) == 6:
				break									
			pedido = input('Faça o pedido corretamente! Peça novamente: ').upper()
								
		while cont < len(pedido):
			num = randint(2,10)
			if num not in numeros:
				numeros.append(num)
				churrasco[num] = pedido[cont]
				cont +=1
			
		geral+=1		
		list_churras.append(f'{churrasco[0]}{churrasco[1]}{churrasco[2]}{churrasco[3]}{churrasco[4]}{churrasco[5]}{churrasco[6]}{churrasco[7]}{churrasco[8]}{churrasco[9]}{churrasco[10]}{churrasco[11]}{churrasco[12]}')
	print()
	for c in list_churras:
		print(c)
		if 'O' in c:
			conto +=1
		else:
			contx += 1
			
	print()		
	print(f'Churrascos com carne:{conto}\nChurrasco vegano: {contx}')
					
		
grill()		