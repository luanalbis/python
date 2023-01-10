temp =[]
notas = []
todos = []
notas = []
cont = 0
while True:
	resp = input('Cadastrar Aluno?[S/N]: ').lower()[0]
	while resp not in 'sn':
		resp = input('Erro! Continuar?[S/N]: ').lower()[0]
	if resp == 'n':
		break
			
	temp.append(input('\nNome: '))
	notas.append(float(input('Nota 1: ')))
	notas.append(float(input('Nota 2: ')))
	print(' ')
	temp.append(notas[:])
	todos.append (temp[:])
	temp.clear()
	notas.clear()	
		
print(' ')
print('='*30)
print('      MÉDIA DOS ALUNOS: ')
print('='*30)

while cont < len(todos):
	sub = len(todos[cont][0])
	print('|{:<1}°|  {:>3} {:>13}'.format(cont +1,todos[cont][0].upper(),(todos[cont][1][0]+ todos[cont][1][1])/2))
	cont += 1
	
while True:
	
	aluno = int(input('\nMostrar notas de qual aluno?: (Numero errado Iterrompe!) '))
	if aluno > len(todos) or aluno < 1:
		'Obrigado por me utilizar?'
		break
	print ('As notas de {} são {}'.format(todos[aluno-1][0].upper(),todos[aluno-1] [1]))

	
	


