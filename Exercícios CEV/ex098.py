from time import sleep
def contador():
	cont = 0
	print('Contagem de 1 ate 10 de 1 em 1')
	for c in range(1,11,1):
		print(c,end=' ')	
	print('FIM')
	print('\n\nContagem de 10 ate 0 de 2 em 2')	
	for c in range(10,-2,-2):
		print(c,end=' ')
	print('FIM!')
	print('\n\nAgora é sua vez de personalisar a contagem!\n')
	
	inicio = int(input('Inicio: '))
	fim = int(input('Fim: '))
	passo = int(input('Passo: '))
	
	if passo == 0:
		passo = passo +1	
	if inicio > fim and passo > 0:	
		passo = passo * -1		
	if inicio > fim and passo < 0:
		passo = passo* -1
		fim = fim - 1
		passo = passo* -1			
					
	if inicio < fim:
		fim = fim + 1
		
	for pos in range (inicio,fim,passo):		
		print(pos,end=' ')
	print('FIM')			
contador()

	
	
	
	
	

		
	


		
		



