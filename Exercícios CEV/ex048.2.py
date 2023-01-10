soma = 0
conta = 0

num = int(input('Digíte os valor maximo: '))

for c in range(5,num+1,5):
	if c % 2 == 1:
		soma = c + soma
		conta = conta + 1
		
print('A soma dos {} valores é {}'.format(conta,soma))
		