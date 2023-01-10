numero = int(input('Numero: '))

anterior = 0
proximo = 0

while(proximo < numero):
  print(proximo,end= ' ')
  proximo = proximo + anterior
  anterior = proximo - anterior
  if proximo == 0:
    proximo = proximo + 1