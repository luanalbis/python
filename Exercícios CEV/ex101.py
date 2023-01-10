def voto(a):
	data = 2022 - a
	if data < 18:
		return f'Com {data} anos voce tem seu VOTO NEGADO'
	elif data >= 65:
		return f'Com {data} anos seu voto é OPCIONAL'
	else:
		return f'Com {data} anos seu voto é OBRIGATÓRIO'
	
data = int(input('Ano de nascimento: '))
print(voto(data))