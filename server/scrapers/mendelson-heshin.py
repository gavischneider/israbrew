from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#for page in range(1,14):
#{page}
base_url = f'https://mendelson-heshin.com/product-category/%d7%91%d7%99%d7%a8%d7%95%d7%aa/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
}

html = urlopen(base_url).read()
soup = BeautifulSoup(html, features='html.parser')
prods = soup.find('ul', class_='products')
beers = prods.find_all('ul', class_='woo-entry-inner')

#print(beers)

for beer in beers:
    print('\n')
    #print(beer)

    # 1-2. URL and image
    data = beer.find_all('li')
    image_data = data[0]
    link_data = image_data.find('a')
    link = link_data.get('href')
    print(link)
    print('\n')

    img = link_data.find('img').get('data-src')
    print(img)

    # 3. Name
    name_data = data[2]
    name = name_data.find('a').text
    #print(name)
    newtext = name.split(" ")
    arr = [];
    for word in newtext:
        if word.isascii():
            arr.append(word)
        else:
            arr.append(word[::-1])
    name = arr[::-1]
    name = " ".join(name)
    print(name)

    # 4. Price
    price_data = data[3]
    price = price_data.find('bdi').text
    print(price)