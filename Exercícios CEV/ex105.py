def notas(*num,sit=False):	
	dados ={}			
	dados['Tot'] = len(num)
	dados['Maior'] = max(num)
	dados['Men'] = min(num)
	dados['Med'] =float(f'{sum(num)/len(num):.1f}')
	 	
	if sit:	
		if dados['Med'] >=7:
			dados ['Sit'] = 'ÓTIMA'
		if dados['Med'] > 6:
			dados ['Sit'] = 'RAZOAVEL'
		if dados['Med'] < 6:
			dados ['Sit'] = 'RUIM'
		if dados['Med'] < 3:
			dados ['Sit'] = 'HORRÍVEL'
	return dados
		
resp = notas(10,10,10,sit=True)
print(resp)
