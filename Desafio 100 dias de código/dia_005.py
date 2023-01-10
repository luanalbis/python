
def somaPar():
	import math
	lista=[]
	letras = []
	cont = contador = par = 0
	contador
	while True:
		meias = input ('Meias: ').upper()
		while cont < len(meias):

			if meias[cont] not in letras:
				letras.append(meias[cont])										
			cont+=1			
		while contador < len(letras):
			lista.append(meias.count(letras[contador]))
			if lista[contador] /2 > 0.5:
				par += math.trunc(lista[contador] /2)
			contador +=1
		
		if par > 1:	
			return f'{par} pares de meias!'
			
		return f'{par} par de meias!'
		
print(somaPar())

