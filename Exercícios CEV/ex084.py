resposta = ' '
dados =[]
principal = []
pessoas=[]
pesos=[]

while resposta != 'n':
	nome = input('Nome: ')
	peso = int(input('Peso KG: '))
	pessoas.append(nome)
	pesos.append(peso)
	dados.append(nome)
	dados.append(peso)
	principal.append(dados[:])
	dados.clear()
		
	resposta = input('\nContinuar cadastrando? ').lower().strip()[0]
	while resposta not in 'ns':
		resposta = input('Erro. Continuar cadastrando? ').lower().strip()[0]
	if resposta in 'sn':
			print(' ')
					
print('Total de pessoas cadastradas:', len(principal))	

print ('O maior peso foi {:.1f}KG. Peso de {}.'.format(max(pesos),pessoas[pesos.index(max(pesos))]))
print ('O menor peso foi {:.1f}KG. Peso de {}.'.format(min(pesos),pessoas[pesos.index(min(pesos))]))


