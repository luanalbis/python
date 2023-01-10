temp = []
principal =[]
resp = ' '
maior = menor = 0
pesado = []
leve = []

while True:
	temp.append(input('Nome: '))
	temp.append(float(input('Peso KG: ')))
	resp= input('\nContinuar?').lower()[0]
	
	if len(principal) == 0:
		maior = menor = temp[1]
	else:
		if temp[1] > maior:
			maior = temp[1]
		if temp[1] < menor:
			menor = temp[1]
		
	principal.append(temp[:])
	temp.clear()
	
	while resp not in 'sn':
		resp= input('Continuar?').lower()[0]
		if resp in 'sn':
			print (' ')
		
	if resp == 'n':
		print('\nObrigado por me utilizar!')
		break

for p in principal:
	if p[1] == maior:
		pesado.append(p[0])
	if p[1] == menor:
		leve.append(p[0])
	
		
print('O numero de cadastrados foi {}'.format(len(principal)))
print ('O menor peso foi {}KG, peso de {} .'.format(menor,leve))
print ('O maior peso foi {}KG, peso de {} .'.format(maior,pesado))
				
						
	

