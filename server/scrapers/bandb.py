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
    

    # Get beer image
    img = beer.find_all('div', class_='grid__image-ratio')
    if(img):
        links = re.findall(r'(//cdn.shopify.com\S+)', str(img))
        print(links[0])

        # Get beer url
        l = beer.get('href')
        link = product_base_url + l
        print(link)
    # Get beer data
    data = beer.find('div', class_='grid-product__meta')
    if(data):

        # 1. Beer name
        name = data.find_all('div')[0].text
        if '-' in name:
            newtext = name.split('-') #[1]
            if len(newtext) > 2:
                # Reverse Hebrew text
                n = [];
                for word in newtext:
                    if word.isascii():
                        n.append(word)
                    else:
                        n.append(word[::-1])
                newtext = n[-1]
            else:
                newtext = name.split('-')[1]
        else:
            newtext = name.split(' ') #[1]
            # Reverse Hebrew text
            n = [];
            for word in newtext:
                if word.isascii():
                    n.append(word)
                else:
                    n.append(word[::-1])
            newtext = n[::-1]
            newtext = " ".join(newtext)
        name = newtext
        if name[0] == " ":
            name = name[1:]       

        # 2. Brewery
        brewery = data.find_all('div')[1].text
        if ' ' in brewery:
            a = []
            newbrewery = brewery.split(' ')
            for word in newbrewery:
                if word.isascii():
                    a.append(word)
                else:
                    a.append(word[::-1])
            brewery = a #[::-1]

            all_hebrew = True
            for w in brewery:
                if w.isascii():
                    all_hebrew = False
            if all_hebrew:
                brewery = brewery[::-1]

            brewery = " ".join(brewery)
        else:
            if not brewery.isascii():
                brewery = brewery[::-1]

        # 3. Price
        price = data.find_all('div')[2].text
        if not price[0].isascii():
            price = price[6:]
        np = price.split(" ")
        price = np[::-1]
        price[0] = price[0][0]
        price = " ".join(price)

        print(name)
        print(brewery)
        print(price)
        print('\n')