from random import shuffle
n1 = input ('Aluno 1: ')
n2 = input ('Aluno 2: ')
n3 = input ('Aluno 3: ')
n4 = input ('Aluno 4: ')

lista = [n1, n2, n3, n4]
shuffle(lista)

print (f'A ordem de apresentação será:\n {lista}')

#shuffle = embaralhar, ou seja, a ordem foi embaralhada pelo comando

