from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from chompjs import parse_js_object
import json

def scrape_tiv_taam():
    results = []
    supplier = 'Tiv Taam'

    # base_url is the beer page, but base_url2 is the script that loads the beers
    base_url = f'https://www.tivtaam.co.il/categories/90315/products'
    base_url2 = 'https://www.tivtaam.co.il/v2/retailers/1062/branches/924/categories/90315/products?appId=4&categorySort=%7B%22sortType%22:2,%22topPriority%22:%22%5B%7B%5C%22id%5C%22:14049%7D,%7B%5C%22id%5C%22:42411%7D,%7B%5C%22id%5C%22:18410%7D,%7B%5C%22id%5C%22:24550%7D,%7B%5C%22id%5C%22:32493%7D%5D%22%7D&categorySort=%7B%22sortType%22:7%7D&from=24&languageId=1&minScore=0&names=%D7%91%D7%99%D7%A8%D7%95%D7%AA&names=Beers&names=%D0%9F%D0%B8%D0%B2%D0%BE&names=%D7%A2%D7%95%D7%9C%D7%9D+%D7%94%D7%91%D7%99%D7%A8%D7%94,+%D7%99%D7%99%D7%9F+%D7%95%D7%90%D7%9C%D7%9B%D7%95%D7%94%D7%95%D7%9C&names=Wine+beer+alcohol%26cigarettes&names=%D0%92%D0%B8%D0%BD%D0%BE+%D0%B8+%D0%B0%D0%BB%D0%BA%D0%BE%D0%B3%D0%BE%D0%BB%D1%8C&size='
    base_url_product = 'https://www.tivtaam.co.il/categories/90315/products?catalogProduct='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
    }

    html = urlopen(base_url2 + '19').read()
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
        #print(beer)

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
        #print('\n')

        #db.session.add(new_beer)  
        #db.session.commit() 

    #print(f'Total printed: {len(beers)}')
    return results
    print(f"Finished scraping: {supplier}!")

#scrape_tiv_taam()