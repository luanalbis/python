nome = str(input('Qual seu nome?')).lower()

L = nome.find('silva')

print(' ')

if nome.find('silva') >= 0:
	print ('Possui')
else:
	print (' Não possui')
