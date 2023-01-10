print ('='*25)
print('Vamos jogar PAR ou IMPAR!')
print('='*25)

from random import randint
resultado = ' '
par = ' '
impat = ' '
escolhapc =' '
partida =' '
cont = 0

while True:
	
	num = int(input('Digíte um número: '))
	escolha = input('PAR ou IMPAR? (P/I)').upper()
	print(' ')
	pc = randint(1,10000)
	soma = pc + num
	
	if soma %2 == 0:
		resultado = 'PAR'
	if soma % 2  == 1:
	   resultado = 'IMPAR'
	   
	if escolha == 'I':
	 escolha = 'IMPAR'
	 escolhapc = 'PAR'	  
	 
	if escolha == 'P':
	 	escolhapc = 'IMPAR'
	 	escolha = 'PAR'
	 	
	if resultado == 'IMPAR' and escolha == 'IMPAR' or resultado == 'PAR' and escolha == 'PAR':
		partida = 'GANHOU'
		
	if resultado == 'PAR' and escolha == 'IMPAR' or resultado == 'IMPAR' and escolha == 'PAR' :
		partida = 'PERDEU'
	
	if partida == 'GANHOU':
	     cont = cont + 1
	     
	  
	
	print('='*50) 
	print(f'Sua escolha {num}/{escolha} e a do programa foi {pc}/{escolhapc}\nResultado:{soma} é {resultado},voçê {partida}.')
	print('='*50) 
	print(' ')
	
	print(f'Vitórias consecutivas:{cont}')
	print (' ')
	
	if partida == 'PERDEU':
	   print('VOÇÊ PERDEU!')
	   break	   
	print('Vamos novamente...')	 
	print(' ')
	
	
	
	