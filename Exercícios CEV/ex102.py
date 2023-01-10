def fatorial(a,show = True):
		f = 1
		for c in range (a,0,-1):
			f = f*c	
			if show:
				print(c, end='')
				if c > 1:
					print(' x ',end= '')
				else:
					print(' = ',end= '')
		print(f)
fatorial(int(input('Número pra fatorar:')))



		
	

