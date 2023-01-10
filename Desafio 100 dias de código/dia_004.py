def progresso():
	kms =[]
	cont = 1
	for c in range (0,5):
		km = int(input('Kms '))
		kms.append(km)
		if kms[c] > kms[c-1]:
			cont += 1
			
	print(f'Dias de progresso {cont-1}')
	
progresso()

