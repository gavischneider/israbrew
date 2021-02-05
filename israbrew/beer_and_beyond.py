from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json

from israbrew.models import Beer

def scrape_beer_and_beyond():
    results = []

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

        # 1. Get beer image
        img = beer.find_all('div', class_='grid__image-ratio')
        if(img):
            links = re.findall(r'(//cdn.shopify.com\S+)', str(img))
            img_link = links[0]
            img_link = img_link[2:]
            img_link = 'https://' + img_link
            #print(img_link)

            # 2. Get beer url
            l = beer.get('href')
            link = product_base_url + l
            #print(link)

        # Get beer data (which holds the info we need)
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
                    n.append(word)
                 
                newtext = " ".join(newtext)
            name = newtext
            if name[0] == " ":
                name = name[1:]       

            # 2. Brewery
            brewery = data.find_all('div')[1].text
            # if ' ' in brewery:
            #     a = []
            #     newbrewery = brewery.split(' ')
            #     for word in newbrewery:
            #         a.append(word)
            #     brewery = a 

            #     brewery = " ".join(brewery)

            # 3. Price
            price = data.find_all('div')[2].text
            if not price[0].isascii():
                price = price[6:]
            np = price.split(" ")
            price = np[::-1]
            # Tak the NIS symbol only
            price[0] = price[0][0]
            price = " ".join(price)

            #print(name)
            #print(brewery)
            #print(price)
            print('\n')

            new_beer = Beer(name, price, link, img_link, brewery)

            print("-----------------Beer Class------------------")
            print(new_beer)
            print(new_beer.name)
            print(new_beer.price)
            print(new_beer.url)
            print(new_beer.image)
            print(new_beer.brewery)
            results.append(json.dumps(new_beer.__dict__))

    print(results)    
    return results