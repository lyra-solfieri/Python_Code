import requests
from bs4 import BeautifulSoup

#Letra da música Beautiful Soup 

url = 'ttps://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'

#Solicitação da página da música atribuida a uma variável 
pagina = requests.get(url)

# Usando o módulo Beautiful Soup
sopa = BeautifulSoup(pagina.text, 'html.parser')

# Para mostrar o conteúdo da página com o método prettify()

print(sopa.prettify())

# encontrar instâncias de uma tag  com o método find_all

sopa.find_all('p')
