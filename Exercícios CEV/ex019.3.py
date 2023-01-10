import random

print ('SORTEIO!!')
print (' ')
print ('Iremos realizar um sorteio com base nas pessoas que escolher:' )

A = input ('Aluno 1: ')
AA = input ('Aluno 2: ')
AAA =input('Aluno 3: ')
AAAA = input ('Aluno 4: ')

print(' ')
print(f'Os alunos escolhidos foram: {A},{AA},{AAA} e {AAAA}.')

pessoas = [ A , AA,AAA,AAAA ]

sorteio = random.choice(pessoas)

print(' ')
print (f'Parabéns {sorteio} voçê foi o grande vencedor do SORTEIO!')
print('')
print('Agora vá limpar o quadro KKKKKKKK')

#usei o random.choice para realizar o sorteio