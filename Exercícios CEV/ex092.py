dados = {}
aposent = idade = 0
clt = 1
while True:
	dados['Nome'] = input('Nome: ')
	idade = int(input('Ano de Nascimento:'))
	dados['Idade'] = 2022 - idade
	
	clt = int(input('Carteira de Trabalho (0 não tem): '))
	
	if clt == 0:
		dados['ctps'] = clt
		break
	
	if clt > 0:
		dados['ctps'] = clt
		
	dados['Contratação'] = int(input('Ano de contratação: '))
	dados['Salário'] = int(input('Salário: '))
	dados['Aposentadoria'] = (35 - (2022 - dados['Contratação'])) + (2022 - idade)
	break
	
for k,v in dados.items():
	print('- {} tem o valor {}'.format(k,v))
	