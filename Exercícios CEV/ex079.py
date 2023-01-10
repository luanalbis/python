lista = []
resposta = ' '
cont = 0

while resposta != 'n':
	num = int(input('Número: '))

	if num not in lista:
		lista = lista + [num]
		print('Número adcionado :)\n')
		cont += 1
	else:
		print('Número repetido!\n')
	resposta = input('Continuar?(S/N): ').lower().strip()[0]
	
	while resposta not in ('SsnN'):
			resposta = input('Continuar?(S/N): ').lower().strip()[0]
				
print('\n\nNúmeros digitados: {}\n\nNumeros em ordem {}'.format(cont,sorted(lista)))
		
	
			
 

		

	
	