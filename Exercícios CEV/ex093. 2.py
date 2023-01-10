dados = {}
gols= []
soma = cont = 0

dados['Nome']=input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou?: '))
print()
cont = 0
for c in range (0,partidas):
	gol = int(input(f'Quantos gols na partida {c+1}? '))
	gols.append(gol)
	soma += gol
	
dados['Gols'] = gols
dados ['Total'] = soma

for k,v in dados.items():
	if k == 'Nome':
		print(f'\nO jogador {v} jogou {partidas} partidas \n')
	if k == 'Gols':
		while cont < partidas:
			print('>>>> Na partida {}, meteu {} gols'.format(cont+1,gols[cont]))
			cont+=1
	if k == 'Total':
		print('\nO total de gols foi {}'.format(soma))
		
		
		
	
	
	



	

		