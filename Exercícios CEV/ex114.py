import urllib
import urllib.request

try:
	site = urllib.request.urlopen('https://www.google.com.br')
except:	
	print('Erro')
		
else:
	print('Tudo ok')
	print(site.read())
		
	