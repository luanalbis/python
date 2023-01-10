def Primo():
	num = int(input('Numero: '))
	tot = cont = 0 
	while True:
			cont+=1
			if num % cont == 0:
				tot +=1
				if tot == 2 and num == cont or num ==1:
					return num
				elif tot > 2 and num == cont:
					tot = cont = 0
					num+=1
					continue											
print(Primo())
		
	