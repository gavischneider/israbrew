from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#for page in range(1,14):
#{page}
base_url = f'https://www.biratenu.com/%D7%97%D7%A0%D7%95%D7%AA-2'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
}

html = urlopen(base_url).read()
soup = BeautifulSoup(html, features='html.parser')
prods = soup.find('ul', class_='_3Xnzg')
beers = prods.find_all('li')
#print(beers)

for beer in beers:
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(beer)
    print("")