# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa irá perguntar o VALOR da casa, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar. 

# Calcule o valor da prestacao, sabendo que o valor da parcela nao pode exceder 30% do salário!

casa = float (input('Valor da Casa: '))
sal = float(input('Valor do Salário: ' ))
anos = int (input ('Quantos anos: '))

prestacao = casa/(anos*12)

vp = 0.30*sal

if prestacao<vp:
	print ('O seu empreéstimo foi APROVADO e o valor da parcela será: R${:.2f} em {} anos :) '.format(prestacao, anos))
else:
	print('Me desculpe, mas seu empréstimo foi NEGADO! :( ')
		