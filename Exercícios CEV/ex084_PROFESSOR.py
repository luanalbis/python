temp = []
principal = []
maior = menor = 0
nomep = []
nomel = []

while True:
	temp.append(input('Nome: '))
	temp.append(float(input('Peso em KG: ')))
	if len(principal) == 0:
		maior = menor = temp[1]
	else:
		if temp[1] > maior:
			maior = temp[1]
		if temp[1] < menor:
			menor = temp[1]
		
	principal.append(temp[:])
	temp.clear()
	
	resposta = input('\nContinuar?: ').lower().strip()[0]
	while resposta not in 'sn':
		resposta = input('Erro,Continuar?: ').lower().strip()[0]
	if resposta =='s':
		print(' ')
	if resposta =='n':
		print(' ')
		break
		
for peso in principal:
	if peso[1] == maior:
		nomep.append(peso[0])
		
	if peso[1] == menor:
		nomel.append(peso[0])
	
print(f'Foram registrados um total de {len(principal)} pessoas\n')
print(f'O maior peso foi {maior}KG, peso de {nomep}\n')
print(f'O menor peso foi {menor}KG, peso de {nomel}\n')
	
		

	
	
	
	