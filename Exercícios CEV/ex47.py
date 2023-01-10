n = int(input ('Prepare-se para a contagem regressiva, digite os segundos: '))
from time import sleep
for c in range(n,-1,-1):
	print('Tempo: {}'.format(c))
	sleep(1)

print(' ')
print ('BOOOM!! A BOMBA EXPLODIU')
	