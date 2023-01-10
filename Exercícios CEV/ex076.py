comidas = ('Ovo',0.50, 'Pão',0.60,'Frango',10,'Chiclete',0.20,'Cachorro',100,'Pulga',2,'Jambo',5)
print('-'*35)
print('         TABELA DE PREÇOS')
print('-'*35)
print(' ')
contador = 1
comida =0
preco = 1

while contador < 8:
	print(comidas[comida],'-'* (30 - (len(comidas[comida]))),'R${:.2f}'.format(comidas[preco]))
	
	preco +=  +2
	contador +=1
	comida +=2

	
	
