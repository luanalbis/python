#You're given a string of words. You need to find the word "Nemo", return a string informing [ I found Nemo ] ,if you cant finde Neml, return- i cant find Neml :(

def AcheNemo():
	try:
		nome = input('Frase? ').split()
		if 'Nemo' in nome:
			return f'Encontramos o Nemo, posição {nome.index("Nemo")+1}'			
		return 'Não encontramos o Nemo'							
	except ValueError:
		return 'Não encontramos o Nemo'
				
print(AcheNemo())