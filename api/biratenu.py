from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json

def scrape_biratenu():
    results = []
    supplier = 'Biratenu'
    # Asking for more pages than we need - this will give us all the products in one shot
    base_url = f'https://www.biratenu.com/%D7%97%D7%A0%D7%95%D7%AA-2?page=20'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
    }

    html = urlopen(base_url).read()
    soup = BeautifulSoup(html, features='html.parser')
    prods = soup.find('ul', class_='_3Xnzg')
    beers = prods.find_all('li')

    for beer in beers:
        # 1. Image
        img = beer.find('div', class_='_3-5SE').get('style')
        img = re.sub('^background-image\:url\(', '', img)
        img = re.sub('\);background-size:cover$', '', img)
        img = re.sub('w_100', 'w_222', img)
        img = re.sub('h_100', 'h_222', img)

        # 2. url
        url = beer.find('a').get('href')

        # 3-4: Name and Brewery
        text = beer.find('h3').text
        if '-' in text:
            newtext = text.split('-')
            brewery = newtext[0] 
            name = newtext[1] 
        else:
            if " " in text:
                newtext = text.split(" ")

                # Check if there was more than one space
                if len(newtext) > 2:
                    newtext = text
                    name = newtext
                    brewery = " "
                else:
                    brewery = newtext[0]
                    name = newtext[1] 
            else:
                name = text
                brewery = ""

        # 5. Price
        price = beer.find('span', class_='_23ArP').text
        nis = price[-1]
        price = price[:-1]
        price = nis + " " + price

        new_beer = [name, price, url, img, supplier, brewery]
        results.append(new_beer)
        
    return results
    print(f"Finished scraping: {supplier}!")
