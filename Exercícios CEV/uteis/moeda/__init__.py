def dobro(num,format=False):
	r = num*2
	if format is True:
		return moeda(r)	
	if format is False:
		return  r
	

def metade(num,format=False):
	r = num/2
	if format is True:
		return moeda(r)	
	if format is False:
		return  r


def aumenta10(num,format=False):
	r = num+(num*0.10)
	
	if format is True:
		return moeda(r)	
	if format is False:
		return  r
	
	
def diminui15(num,format=False):
	r = num - (num*0.15)
	if format is True:
		return moeda(r)	
	if format is False:
		return  r


def moeda(r):
	r = (f'R${r:.2f}'.replace('.',','))
	return r
	
def resumo(preco,aumento,desconto):
	print('='*30)
	print('       RESUMO DO VALOR')
	print('='*30)
	print(f'Preço analisado: {moeda(preco)}')
	print(f'Dobro do preço: {(dobro(preco,True))}')
	print(f'Metade do preço: {(metade(preco,True))}')
	print(f'{aumento}% de aumento: {moeda(preco+(preco*(aumento/100)))}')
	print(f'{desconto}% de desconto: {moeda(preco-(preco*(desconto/100)))}')
	