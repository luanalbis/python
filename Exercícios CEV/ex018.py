import math
A = float ( input ('Digíte o valor do Ângulo: '))
AN = math.radians (A)

print (' ')
print ('Baseado no ângulo informado podemos concluir que:')
print (' ')
print (f'Seu cosseno é: {math.cos(AN):.4f}')
print (f'Seu seno é: {math.sin(AN):.4f}')
print (f'Sua tangente é: {math.tan(AN):.4f}')

# - A fórmula do cossenl,seno e tangente só funciona com radiando,ou seja, use primeiro a formula math.radians() para descobrir o radiano do angulo