dados = {}
dados['nome'] = input('Nome: ')
dados['media'] = float(input('Média: '))
situacao = ' '
if dados['media'] >7:
	dados['situacao'] = 'Aprovado'
else:
	dados['situacao'] = 'Reprovado'

print('\nNome do aluno: {}'.format(dados['nome']))
print ('Média do aluno {}'.format(dados['media']))
print('Situação do aluno: {}'.format(dados['situacao']))
print(' ')

for k,v in dados.items():
	print('{} é igual {}'.format(k,v))
	
	