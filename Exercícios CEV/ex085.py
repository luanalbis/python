lista = ([],[])
cont = 0



while cont < 7:
	num = int(input('Número: '))
	if num % 2 ==0:
		lista[0].append(num)
	else:
		lista[1].append(num)
	
	cont = cont+1
	
print(sorted(lista[0]),sorted(lista[1]))





		