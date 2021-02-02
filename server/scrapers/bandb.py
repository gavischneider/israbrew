from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#for page in range(1,14):
#{page}
base_url = f'https://beerandbeyond.com/collections/all-beers?page=1'
product_base_url = 'https://beerandbeyond.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
}

html = urlopen(base_url).read()
soup = BeautifulSoup(html, features='html.parser')
prods = soup.find('div', id='CollectionSection')
beers = prods.find_all('a')
#print(beers)

for beer in beers:
    

    #Get beer image
    img = beer.find_all('div', class_='grid__image-ratio')
    if(img):
        links = re.findall(r'(//cdn.shopify.com\S+)', str(img))
        print(links[0])

        # Get url
        l = beer.get('href')
        link = product_base_url + l
        print(link)
    # Get beer data
    data = beer.find('div', class_='grid-product__meta')
    if(data):
        name = data.find_all('div')[0].text
        brewery = data.find_all('div')[1].text
        price = data.find_all('div')[2].text
        print(name)
        print(brewery)
        print(price)