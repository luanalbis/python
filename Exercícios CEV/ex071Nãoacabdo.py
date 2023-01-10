valor = 1
cont50 = 0
cont20= 0
cont10 = 0
cont1 = 0

while valor >= -1:
	valor = int(input('Valor para sacar:R$'))
	print(' ')
	while valor >= 1:
		valor = valor - 1
		cont1 = cont1 + 1
		while valor >= 10:
			valor = valor -10
			cont10 = cont10 + 1
			while valor >= 20:
				valor = valor - 20
				cont20 = cont20 + 1
				while valor >= 50:
						valor = valor - 50
						cont50 = cont50 + 1
					
							
	print (f'Total de {cont50} cédulas de R$50')
	print (f'Total de {cont20} cédulas de R$20')
	print (f'Total de {cont10} cédulas de R$10')
	print (f'Total de {cont1} cédulas de R$1')
	print(' ')				
							        
							         

