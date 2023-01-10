lista = ([],[],[])
cont = indice = matriz = somapar = c3 = 0
maior = []

while cont < 3:
	
	while matriz < 3:
		num = int(input(f'Digíte um valor para [{cont}, {matriz}]: '))
		lista[indice].append(num)
		matriz = matriz + 1
		
		if num % 2 == 0:
			somapar += num
		if cont == 2:
			c3 += num
		if cont ==1:
			maior.append(num)		
		
	cont = cont+1
	matriz = matriz - 3
	indice = indice + 1

print('\n[{}] [{}] [{}]\n[{}] [{}] [{}]\n[{}] [{}] [{}]'.format(lista[0][0],lista[0][1],lista[0][2],lista[1][0],lista[1][1],lista[1][2],lista[2][0],lista[2][1],lista[2][2]))

print ('Soma dos pares: {}'.format(somapar))
print('Soma Terceira coluna: {}'.format(c3))
print('Maior valor Segunda coluna: {}'.format(max(maior)))