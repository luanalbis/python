lista = ('LISTA', 'APRENDER', 'LUAN','AMANDA' )

for tupla in lista:
	print (f'\nNa palavra {tupla} temos:',end=(' '))
	
	for letras in tupla:
		if letras.lower() in ('aeiou'):
			print(letras,end=(' '))

		