tabela = ('Ceará','Corinthians','Grêmio','Internacional','Bahia','Fortaleza','Fluminense','Atletico MG','Botafogo','Cruzeiro','Santos','Bragantino','Coritiba','Flamengo','Vasco','São Paulo','America MG','Athletico PR','Palmeiras','Chapecoense')

print('Times classificados para LIBERTADORES:\n{}'.format(tabela[:5]))
print(' ')

print('Os 4 últimos colocados:\n{}'.format(tabela[-4:]))

print(' ')
print ('Times em ordem alfabética:\n{}'.format(sorted(tabela)))

print(' ')
print('Posição da Chapeconse: {}° Posição'.format(tabela.index('Chapecoense')+1))