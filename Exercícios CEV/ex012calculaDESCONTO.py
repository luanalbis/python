v = float(input ('Valor do produto: '))
d = float(input ('Porcentagem do desconto: '))

dv = d/100
nv = v-(v*dv)

print ('O produto com desconto ficará:R${:.2f}'.format(nv))