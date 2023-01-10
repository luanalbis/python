#mostre a categoria das idades
#ate 9 anos - miirim
#ate 14 anos - infantil
#ate 19 anos - junior
#ate 20 anos senior
#acima - master

ano = int(input('Digíte o ano dr nascimento: '))
idade = 2022 - ano

print('Sua idade: {}'.format(idade))
if idade <=9:
	print('Sua classificação: MIRIM!')
	
elif idade > 9 and idade < 15:
	print ('Sua classificação: JÚNIOR!')
	
elif idade >= 15 and idade <=20:
	print ('Sua classificação: SÊNIOR!')
	
else:
	print ('Sua classificação: MASTER!')
	
	
