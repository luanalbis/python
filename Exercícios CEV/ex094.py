dados = {}
principal = []
soma = cont = 0
mulher =[]
while True:
	
	dados[f'Nome'] = nome = input('Nome?: ')
	
	while True:
		dados[f'Sexo'] = sexo = input('Sexo:[M/F] ').upper().strip()[0]
		
		if sexo in 'MF':
			break
	dados[f'Idade'] =idade = int(input('Idade: '))
	soma += dados['Idade']
	print()
	
	if sexo == 'F':
		mulher.append(nome)
			
	while True:
		resp = input('Continuar?[S/N]').upper().strip()[0]
		if resp in 'SN':
			print()
			break
			
	principal.append(dados)
	dados = {}
	if resp == 'N':
		print('Carregando dados :)')
		break

print('A) Pessoas cadastradas:',len(principal))
print('B) Média de idade: {:.1f} anos'.format(soma/len(principal)))
print('C) Mulheres cadastradas: {}'.format(mulher))
print('D) Lista de pessoas acima da média:\n')

for k,v in enumerate(principal):
	
	if v['Idade'] > soma/len(principal):
		for k,p in v.items():
			print('{} = {} |'.format(k,p),end=(' '))
			cont += 1
			if cont % 3 ==0:
				print(' ')
		

		
		


