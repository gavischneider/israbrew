from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
#from israbrew.models import Beer
from chompjs import parse_js_object
import json
#from . import db

def scrape_keshet_teamim():
    results = []
    supplier = 'Keshet Teamim'

    # First delete existing beers, then scrape and add the new ones
    #.query.filter(Beer.supplier == 'Keshet Teamim').delete()
    #db.session.commit() 

    # base_url is the beer page, but base_url2 is the script that loads the beers
    base_url = f'https://www.keshet-teamim.co.il/categories/79678/products'

    base_url2 = 'https://www.keshet-teamim.co.il/v2/retailers/1219/branches/1437/categories/79678/products?appId=4&categorySort=%7B%22sortType%22:2%7D&from=0&languageId=1&minScore=0&names=%D7%91%D7%99%D7%A8%D7%94&names=%D0%9F%D0%B8%D0%B2%D0%BE&names=%D7%99%D7%99%D7%A0%D7%95%D7%AA+%D7%95%D7%90%D7%9C%D7%9B%D7%95%D7%94%D7%95%D7%9C&names=%D0%92%D0%B8%D0%BD%D0%B0+%D0%B8+%D0%B0%D0%BB%D0%BA%D0%BE%D0%B3%D0%BE%D0%BB%D1%8C&names=%D7%9E%D7%A9%D7%A7%D7%90%D7%95%D7%AA&names=%D0%9D%D0%B0%D0%BF%D0%B8%D1%82%D0%BA%D0%B8+%D0%B8+%D0%B0%D0%BB%D0%BA%D0%BE%D0%B3%D0%BE%D0%BB%D1%8C&size='

    base_url_product = 'https://www.keshet-teamim.co.il/categories/79678/products?catalogProduct='

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
    }

    # First request - we need this to see how many products there are
    html = urlopen(base_url2 + '16').read()
    soup = BeautifulSoup(html, features='html.parser')
    parsed = parse_js_object(str(soup))
    total = parsed['total']

    print(f'We got the total: {total}')

    # Now that we know how many products there are, request them
    new_url = base_url2 + str(total)
    html = urlopen(new_url).read()
    soup = BeautifulSoup(html, features='html.parser')
    beers = parse_js_object(str(soup))['products']

    for beer in beers:

        # Name
        name = beer['localName']
        print(name)

        # Brewery
        if 'brand' in beer:
            brewery = beer['brand']
            if 'names' in brewery:
                brewery = brewery['names']
                if '1' in brewery:
                    brewery = brewery['1']
                else:
                    brewery = ""
            else:
                brewery = ""
        else:
            brewery = ""
        print(brewery)

        # Price
        if 'branch' in beer:
            price = beer['branch']
            if 'regularPrice' in price:
                price = str(price['regularPrice']) + '0'
            else:
                price = ""
        else:
            price = ""
        print(price)

        # Image
        if "image" in beer:
            img = beer['image']
            if "url" in img:
                img = img['url']
                img = re.sub(r'\{\{size\}\}', 'medium', img)
                img = img.split('{{', 1)[0]
                img = img + 'jpg'
            else:
                img = ""
        else:
            img = ""
        print(img)

        # URL
        if 'productId' in beer:
            id = beer['productId']
            url = base_url_product + str(id)
        else:
            url = ""
        print(url)

        print('\n')

        new_beer = [name, price, url, img, supplier, brewery]
        results.append(new_beer)
        #results.append(json.dumps(new_beer.__dict__))

        #db.session.add(new_beer)  
        #db.session.commit() 

    #print(f'Total printed: {len(beers)}')
    return results
    print(f"Finished scraping: {supplier}!")

#scrape_keshet_teamim()