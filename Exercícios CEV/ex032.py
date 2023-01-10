ano = input ('Ano: ')
bissexto = ano[-2:]
bissexto = int (bissexto)
if (bissexto%4) == 0:
	print(' O ano é bissesxto!')
else:
	print(' O ano não é bissesxto!')