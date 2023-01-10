cidade = input('Digite o nome da cidade:').lower()
dividido = cidade.split()

if dividido[0] == 'santo':
	print('Possui')
else:
	print('Não possui')
	
cid = str(input('Digíte o nome da cidade:')).strip().upper()

print(cid[:5]== 'SANTO')