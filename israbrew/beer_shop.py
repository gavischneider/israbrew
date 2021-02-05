from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
#from israbrew.models import Beer
import json
def scrape_beer_shop():
    results = []

    #for page in range(1,14):
    #{page}
    base_url = f'https://www.beershop.co.il/%d7%aa%d7%a4%d7%a8%d7%99%d7%98-%d7%91%d7%99%d7%a8%d7%94/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
    }

    html = urlopen(base_url).read()
    soup = BeautifulSoup(html, features='html.parser')
    prods = soup.find('div', class_='section-items-container')

    print(soup)

    #beers = prods.find_all('div', class_='menu-item')

    #for beer in beers:
     #   print(beer)
      #  print('-----------------------------')

scrape_beer_shop()