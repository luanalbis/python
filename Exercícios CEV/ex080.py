lista= []
for c in range(0,5):
	num = int(input('Número: '))
	
	if c == 0 or num > max(lista):
		lista.append (num)
		
	else:
		for pos, numero in enumerate(lista):
			if num < numero:
				lista.insert(pos,num)
				break
			

print(lista)



