termo = int(input('Primeiro termo: '))
razao = int(input ('Razão: '))

contador = 0

print(termo,end=' > ')	

while contador < 10:

	print(termo+razao, end=' > ')
	termo = termo + razao
	contador = contador + 1
print('FIM')