import random
pesos = []
for c in range (0,5):
	peso=float(input('Qual os pesos? '))
	pesos = pesos + [peso]

print('O maior peso foi:',max(pesos))
print ('O menor peso foi:',min(pesos))
	
