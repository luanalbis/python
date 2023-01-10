def dobro(num,format=False):
	r = num*2
	if format is True:
		return moeda(r)	
	if format is False:
		return  r
	

def triplo(num,format=False):
	r = num*3
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


