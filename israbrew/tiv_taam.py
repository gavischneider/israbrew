from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
#from israbrew.models import Beer
import json
def scrape_tiv_taam():
    results = []

    #for page in range(1,14):
    #{page}
    base_url = f'https://www.tivtaam.co.il/categories/90315/products'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
    }

    html = urlopen(base_url).read()
    soup = BeautifulSoup(html, features='html.parser')
    prods = soup.find('div', class_='items')
    #beers = prods.find_all('div', class_='u-1/2')

    print(soup)

scrape_tiv_taam()