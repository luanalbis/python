cont = 0
soma = 0

while True:
	num = int(input('Número: '))
	if num == 999:
		break		
	soma = num + soma
	cont = cont + 1	
	
print(f'A soma é {soma} e o total de numeros foram {cont}')