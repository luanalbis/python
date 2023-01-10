from uteis import moeda

p = float(input('Número: '))
print('O dobro de {} é {}'.format(p,(moeda.dobro(p))))
print('O triplo de {} é {}'.format(p,(moeda.triplo(p))))
print('O valor de {} com 10% de acrescimo é {}'.format(p,(moeda.aumenta10(p))))
print('O valor de {} com 15% a menos é {}'.format(p,(moeda.diminui15(p))))


