vel = int(input('Este é o velocímetro, e seu carro acaba de passar a uma velocidade em KM de: '))

print(' ')
pa = (vel-80)*7.00

if vel > 80:
	print(f'Voçê ultrapassou o limite de 80KM estabelecido.\nLogo, terá que pagar um total de : R${pa}' )