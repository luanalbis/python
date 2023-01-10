import math

soma = 0
cont = 0

for c in range(1,7):
	c = int(input('Número: '))
	if c % 2 == 0:
		soma = c + soma
		cont = cont + 1

print (f'A soma do {cont} numero pares é { soma} ')
		