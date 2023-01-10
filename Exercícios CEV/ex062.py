termo = int(input('Primeiro termo: '))
razao = int(input ('Razão: '))
resposta = 0
contador = 0

print(termo,end=' - ')	

while contador < 10:

	print(termo+razao, end=' - ')
	termo = termo + razao
	contador = contador + 1

	if contador == 10:
		print(' ')
		resposta = int(input('\nGostaria de acrescentar mais quantos termos?'))
		
		if resposta > 0:
			print(' ')
			contador = contador - resposta
		
		if resposta == 0:
			print(' ')
			print('Obrigado,volte mais tarde!')
			
		
	
	
	


