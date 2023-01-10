#elabore um programa que calcule o valor a ser pago por um produto, considerando seu preco normal e condicao de pagamento:

#a vista-10% desconto
#a vista no cartao = 5% desconto
#em ate 2x cartao = preco  normal
#3x ou mais no cartao = 20% de juros

pr = float(input('Valor do produto:R$'))
print (' ')

print('[1] A vista Dinheiro ou Pix')
print ('[2] Cartão 1X')
print ('[3] Cartão 2X')
print ('[4] Cartão 3X ou mais')
print(' ')

forma = int(input('Forma de Pagamento: '))
print(' ')
vista = pr-(pr*0.10)
cartao1x = pr-( pr*0.05)
cartao2x = pr
cartao3x = pr+ (pr*0.20)

if forma == 1:
	print('O valor a vista no DINHEIRO ou PIX ficará com 10% de desconto,\nVALOR A PAGAR: R${:.2f} a VISTA'.format(vista))

elif forma == 2:
	print('O valor a vista no CARTÃO ficará com 5% de desconto,\nVALOR A PAGAR:R${:.2f} a VISTA'.format(cartao1x))

elif forma == 3:
	print ('O valor parcelado em 2X no CARTÃO não terá descontos,\nVALOR A PAGAR:R${:.2f} em 2 parcelas de R${:.2f}'.format(cartao2x,pr/2))

elif forma == 4:
	
	vezes = int(input('Quantas parcelas? '))
	print(' ')
	if vezes < 3:
		print(' ')
		print('Escolha outra forma de pagamento, por favor!')
		
		
	elif vezes > 2:
		print(' ')
		print('O valor parcelado em {}X no CARTÃO terá um acréscimo de 20%,\nVALOR A PAGAR:R${:.2f} em {} parcelas de {:.2f}'.format(vezes, cartao3x,vezes, cartao3x/vezes))

	
else:
	
	print('Forma de pagamento não disponível. Escolha outra, por favor')
	
	








