def ficha(nome,gols):
	return f'O jogador {nome} marcou {gols} gol(s) no campeonato'

n = input('Nome: ').replace(' ','')
g = input('Gols: ')

if n.isnumeric() or not n.isalpha():
	n = '<desconhecido>'
if not g.isnumeric():
	g = 0

print(ficha(n,g))