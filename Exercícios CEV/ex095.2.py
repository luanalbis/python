jogadores = []
dados = {}
gols= []
soma = cont = 0
jog = -1
resp =' '

while True:
	dados['Nome']=input('Nome do jogador: ')
	partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou?: '))
	print()
	for c in range (0,partidas):
		gol = int(input(f'Quantos gols na partida {c+1}? '))
		gols.append(gol)
		soma += gol	
		
	dados['Gols'] = gols
	dados ['Total'] = soma
	jogadores.append(dados)
	dados = {}
	gols = []
	soma = 0
	print( )
	
	while resp not in 'SN':
		resp = input('Continuar?[S/N]: ').upper().strip()[0]
	if resp == 'N':
		print( )
		break
	print()	
	resp =' '
print('Cod      Nome          Gols')
for k,v in enumerate (jogadores):
	print('{: >2}      {: ^7}       {}     Total: {: 1}'.format(k+1,v['Nome'],v['Gols'],v['Total']))
		
while True:
	while True:
		jog = int(input('\nMostrar dados de qual jogador?(999 Encerra)'))
		if jog >=0 and jog <= len(jogadores) or jog == 999:
			break
	if jog == 999:
		print('\nObrigado por utilizar a ferramenta!')
		break
	print('Levantamento do jogador {}'.format(jogadores[jog-1]['Nome']))
	print( )
	cont = 0
	
	for k,v in enumerate(jogadores):
		if v['Nome'] == jogadores[jog-1]['Nome']:
			while cont < len(jogadores[jog-1]['Gols']) :
				print('No jogo {}, meteu {} gols'.format(cont+1,v['Gols'][cont]))
				cont+=1