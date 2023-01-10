soma = 0
maioridade = 0
maisvelho = ' '
mulher = 0

for c in range (1,3):
	print(f'===== PESSOA N°{c} =====')
	nome = input('Nome: ')
	
	sexo = input('Sexo (M/F): ').upper().strip()
	
	idade = int(input('Idade: '))
	soma = idade + soma
	
	print(' ')
	
	if c == 1 and sexo == 'M':
		maioridade = idade
		maisvelho = nome
		
	if sexo == 'M' and idade > maioridade:
		maioridade = idade
		mairvelho = nome
	
	if sexo == 'F' and idade < 20:
		mulher = mulher + 1
	
		
	
	
	
	

print(f'A média de idade do grupo é {soma/4}')
print('O homem mais velho tem {} e se chama {}'.format(maioridade
,maisvelho))
print('Existem {} mulheres com menos de 20 anos na lista'.format(mulher))


	