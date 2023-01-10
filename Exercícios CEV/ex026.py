frase = str(input ('Digite uma frase: ')).lower()

A = frase.count('a')

print ('Nesta frase existem {} letras A, a posição da primeira aparece em {} e a posição da última é {}'.format(A, frase.find('a'),frase.rfind('a')))
