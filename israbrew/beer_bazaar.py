from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from israbrew.models import Beer

#for page in range(1,14):
#{page}
base_url = f'https://beerbazaar.co.il/apps/bundles/bundle/17591'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
}

html = urlopen(base_url).read()
soup = BeautifulSoup(html, features='html.parser')
prods = soup.find('div', id='bundle-builder-app--bundle--root')
#print(prods)
beers = prods.find_all('div')
print(beers)

#for beer in beers:
 #   print("\n")
  #  print(beer)