valor = 100
cont50 = 0
cont20= 0
cont10 = 0
cont1 = 0

while valor > 49:
	valor = int(input('Valor para sacar:R$'))
	print(' ')
	while valor >49:
			valor = valor - 50
			cont50 = cont50 + 1

while valor > 19 < 49:
	valor = valor - 20
	cont20 = cont20+1

while valor > 9 < 20:
	valor = valor - 10
	cont10 = cont10+1
	
while valor > 0 < 10:
	valor = valor - 1
	cont1 = cont1+1


print (f'Total de {cont50} cédula(s) de R$50')
print (f'Total de {cont20} cédula(s) de R$20')
print (f'Total de {cont10} cédula(s) de R$10')
print (f'Total de {cont1} cédula(s) de R$1')
print(' ')

								
							        
							         

