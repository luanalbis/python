#calcule a media de duas notas e mostre a seguinte mensagem no final:
#	
#	media abaixo 5 = reprovado
#	media entre 5.0 e 5.9 = recuperacao
#	media entre 7 ou superior = aprovado

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
m = float((n1+n2+n3)/3)

if m >=7:
	print (f'PARABÉNS, sua média foi {m:.2f} e você está APROVADO')

elif m < 5:
	print(f'OPS, voçê teve uma média {m:.2f} e está REPROVADO!')

else:
	print(f'QUASE, voçê teve uma média {m:.2f} e está de RECUPERAÇÃO')




 
	

