num1 = int (input('Primeiro termo: '))
razao = int (input('Razão: '))
progressao = int(input('Progressão?: '))
ex = razao * progressao

print(' ')
for c in range(num1,ex+1,razao):
	print (c,end=' > ')
	

print ('ACABOU!')