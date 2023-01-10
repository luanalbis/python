from uteis import moeda as m

p = float(input('Número: '))
print('O dobro de {} é R${}'.format(m.moeda(p),(m.moeda(m.dobro(p)))))

print('O triplo de {} é {}'.format(m.moeda(p),(m.moeda(m.triplo(p)))))

print('O valor de {} com 10% de acrescimo é {}'.format(m.moeda(p),(m.moeda(m.aumenta10(p)))))

print('O valor de {} com 15% a menos é {}'.format(m.moeda(p),(m.moeda(m.diminui15(p)))))


