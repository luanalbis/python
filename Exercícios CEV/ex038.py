#Escreva um programa que leia dois numeros inteiros e compare - os, mostrando uma mensagem na tela

n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))

if n1> n2:
	print(f'{n1} é maior que {n2}')
	
elif n2>n1:
	print(f'{n2} é maior que {n1}')
	
else:
	print ('Os dois numeros sao iguais!')