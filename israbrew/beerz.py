from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json

def scrape_beerz():
    results = []
    base_url = f'https://beerzstore.com/collections/%D7%91%D7%99%D7%A8%D7%95%D7%AA?page='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
    }
    supplier = 'BeerZ'

    # Check how many pages there are
    html = urlopen(base_url + '1').read()
    soup = BeautifulSoup(html, features='html.parser')
    pages = soup.find_all('span', class_='page')[-1] 
    pages = int(pages.find('a').text)
    print(pages)

    for page in range(1, pages + 1):
        html = urlopen(base_url + str(page)).read()
        soup = BeautifulSoup(html, features='html.parser')
        prods = soup.find('div', class_='collection-products')
        beers = prods.find_all('div', class_='u-1/2')

        for beer in beers:
            # Image
            image = beer.find('img', class_='product__img').get('data-src')
            image = re.sub('\{width\}', '336', image)
            image = image[2:]
            image = 'https://' + image

            # URL
            url = beer.find('a', class_='product-link').get('href')
            url = 'https://beerzstore.com' + url

            # Name and brewery
            name = beer.find('h3', class_='product__title').text

            # Price
            price = beer.find('span', class_='money') #.text
            if price != None:
                price = price.text
                nis = price[-1]
                price = price[:-1]
                price = nis + " " + price
            else:
                price = ""

            new_beer = [name, price, url, image, supplier, " "]
            results.append(new_beer)
 
    return results
    print(f"Finished scraping: {supplier}!")
