pessoas = 0
homens= 0
mulheres = 0
resposta = 's'
while resposta != 'n':
	
	idade = int(input('Idade: '))
	sexo = input('Sexo:[M/F]')
	resposta = input('Continuar?[S/N]').lower()
	print(' ')
	
	if idade > 18 and sexo == 'm':
		pessoas = pessoas + 1
	if idade > 18 and sexo == 'f':
		pessoas = pessoas + 1
	
	if sexo == 'm':
		homens = homens + 1

	if sexo == 'f' and idade < 20:
		mulheres = mulheres + 1
	
	if resposta == 'n':
		print ('Obrigado por utilizar nossa ferramenta!')
		print (' ')
		
	
		
	
			
					
print(f'Pessoas com +18 anos: {pessoas}')	
print(f'Número de homens cadastrados:{homens}')
print(f'Numero de mulheres com -20 anos:{mulheres}')

		
		
		

		



		
		
	
