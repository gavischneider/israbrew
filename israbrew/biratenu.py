from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from israbrew.models import Beer
import json

def scrape_biratenu():
    results = []

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
        print("\n")
        #print(beer)

        # 1. Image
        img = beer.find('div', class_='_3-5SE').get('style')
        img = re.sub('^background-image\:url\(', '', img)
        img = re.sub('\);background-size:cover$', '', img)
        img = re.sub('w_100', 'w_222', img)
        img = re.sub('h_100', 'h_222', img)
        #print(img)

        # 2. url
        link = beer.find('a').get('href')
        #print(link)

        # 3-4: Name and Brewery
        text = beer.find('h3').text
        if '-' in text:
            # Text is in Hebrew - reverse string
            newtext = text.split('-')
            brewery = newtext[0] 
            name = newtext[1] 
            #print(brewery)
            #print(name)
        else:
            newtext = text.split(" ")
            # Check if there was more than one space
            if len(newtext) > 2:
                newtext = text.join(" ")
                name = newtext
                brewery = " "
            else:
                brewery = newtext[0]
                name = newtext[1]
            #print(newtext)  

        # 5. Price
        price = beer.find('span', class_='_23ArP').text
        #print(price)

        new_beer = Beer(name, price, link, img, brewery)
        results.append(json.dumps(new_beer.__dict__))

    print(results)    
    return results
