#Faça um programa que leia o ano de nascimentl de um jovem e informe, de acordo com sua idade:

#Se ele vai se alistar:
#Se está na hora de alistar
#Se ja passou da hora
# o programa devera mostrar o tempo que falta ou que passou do prazo

data = int(input('Ano de nascimento: ' ))

idade = 2022 -data
falta = 18 - idade
passou = idade - 18

if idade > 18:
	print('Não é possível se alistar pois passou do tempo')
	print('O tempo foi excedido em {} anos'.format(passou))

elif idade < 18:
	print('O alistamento só possível a partir dos 18 anos')
	print(f'Espere mais {falta} anos e volte a se alistar!')
	
else:
	print('Já está na hora de se alistar, procure o quartel mais proximo!')
	
	
 
 