lista = ([],[],[])
cont = indice = matriz = 0


while cont < 3:
	
	while matriz < 3:
		num = int(input(f'Digíte um valor para [{cont}, {matriz}]: '))
		lista[indice].append(num)
		matriz = matriz + 1
		
	cont = cont+1
	matriz = matriz - 3
	indice = indice + 1

print('\n[{}] [{}] [{}]\n[{}] [{}] [{}]\n[{}] [{}] [{}]'.format(lista[0][0],lista[0][1],lista[0][2],lista[1][0],lista[1][1],lista[1][2],lista[2][0],lista[2][1],lista[2][2]))