#1 Usei o input para atribuir uma variavel 'nome'

nome = input ('Qual seu nome completo? ')
print(' ')

#2 Usei o nome.upper para deixar maiusculo e nome.lower para deixar minusculo

print ('Nome maiúsculo:',nome.upper())
print ('Nome minúsculo:',nome.lower())
print(' ')

#3 Atribui uma variavel a dividido, depois dividi atraves do nome.split(), logo em seguida usei o len(dividido) para contar apenas o primeiro nome

dividido = nome.split()
print ('Primeiro nome:',dividido[0][::])
print('Número de letras:',len(dividido[0][::]))

#4 utilizei o nome.replace para substituir o espaco por algo vazio, pra nao contabilizar espacos na contagem'

print(' ')

d1 = nome.replace(' ','')
print ('Número total de letras:',len(d1))

