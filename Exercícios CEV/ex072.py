numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte', 'Não foi possível encontrar')

num = 0
while num != 999:
	while num >=0 <= 20:
		num = int(input('Digíte um número de 0 a 20: '))
		if num == 999:
			print('Finalizando programa...')
			break
		while num < 0 or num > 20:
			num = int(input('Tente novamente,digíte um número de 0 a 20: '))
			
		print ('Seu número por extenso é: {}'.format(numeros[num]))
		print(' ')
		
		
			
	
	
	
	