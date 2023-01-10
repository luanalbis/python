import math
c1 = float(input('Cateto oposto: '))
c2 = float(input('Cateto Adjacente: '))
h = (c1**2) + (c2**2)
hi = math.sqrt (h)
print ('O valor da hipotenusa é: {}'.format(hi))