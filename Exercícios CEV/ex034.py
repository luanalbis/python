sal = int(input('Salário do Funcionário: '))
print (' ')

a1 = (sal/10) + sal
a2 = (sal*0.15) + sal

if sal <= 1250:
	print('PARABÉNS! Seu novo salário será {:.2f}'.format(a2))
else:
	print('PARABÉNS! Seu novo salário será {:.2f}'.format(a1))
