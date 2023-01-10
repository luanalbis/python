#desenvolva uma logica q leia o peso e altura. calcule o IMC e diga se esta saudavel

#formula = peso / altura²
#abaixo 18,5 = abaixo do peso
#entre 18 5 e 25 = peso ideal
#entre 25 e 30 = sobrepeso
#entre 30 e 40 obeso
#acima = obesidade morbida

al = float(input('Qual sua altura?: '))
p = float (input('Qual seu peso?: '))
imc = p/(al*al)
print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
	print ('Voçê está ABAIXO o do peso ideal')

elif imc < 25:
	print('Voçê está no peso IDEAL!')

elif imc < 30:
	print ('Voçê está com SOBREPESO!')

elif imc < 40:
	print('Voçê está com OBESIDADE!')
	
else:
	print('Voçê está com OBESIDADE MÓRBIDA')