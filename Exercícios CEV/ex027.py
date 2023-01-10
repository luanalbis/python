nome = str (input('Olá, digíte seu nome completo,por favor:\n'))

n = nome.split()
u = n[-1]

print('Primeiro nome:{}'.format(n[0]))
print ('Ultimo nome:{}'.format(u))