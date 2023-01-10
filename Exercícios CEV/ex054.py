soma = 0
for c in range (1,8):
	c = int(input('Ano de nascimento: '))

	if 2022 - c >= 21:
		print('Você atingiu a MAIORIDADE!\n')
		soma = soma + 1

	elif 2022 - c < 21:
		print('Voçê ainda NÃO ATINGIU\n')

print(' ')
print('Numero de pessoas maiores de idade : {}'.format(soma))
		