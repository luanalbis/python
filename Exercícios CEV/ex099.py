from random import  randint

def maior(*num):
	maior = cont = 0
	print('='*30)
	print('Valores informados:',end=' ')
	for c in num:
		print (c, end=' ')
		if cont == 0:
			maior = c
		else:
			if c > maior:
				maior = c
		
		cont+=1
	print('\n\nAnalisando os {} valores:'.format(cont))
	print('O maior foi {}.'.format(maior))

		
maior(randint(1,1000),randint(1,1000),randint(1,1000))
maior(randint(1,1000),randint(1,1000),randint(1,1000))



