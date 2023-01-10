km = float(input('Qual a distância da viagem, por favor?: ' ))

print(' ')
p1 = km*0.50
p2 = km*0.45

if km <= 200:
	print('O valor da viagem fica:R${:.2f}'.format(p1))
else:
	print('O valor da viagem ficará:R${:.2f}'.format(p2))
	