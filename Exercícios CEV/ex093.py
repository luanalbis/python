dados = {}
gols= 0
nome = input('Nome do jogador: ')
dados[nome]=int(input(f'Quantas partidas {nome} jogou?: '))
print()
cont = 0
for c in range (0,dados[nome]):
	dados[c+1]= int(input(f'Quantos gols na partida {c+1}? '))
	gols += dados[c+1]
	
dados['Gols'] = gols

for k,v in dados.items():
	
	if k == nome:
		print (f'\nO jogador {k} jogou {v} partidas e marcou {gols} gols. Média de {gols/v:.2f} gols por partida\n.')
		
	if k != nome:
		if k != 'Gols':	
			print(f'    > Na partida {k}, fez {v} gols')
	
	if k == 'Gols':
		print(f'\nTotal de gols: {dados["Gols"]}')
	
		
	
	
		
	
	
	
		
		
		
	
	
	
		
	
	 
		

	

