from bs4 import BeautifulSoup
from urllib.request import urlopen
from chompjs import parse_js_object
#from israbrew.models import Beer
import json
#from . import db

base_url = 'https://beerbazaar.co.il/apps/bundles/bundle/17591'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
}
price = '8 for 99, 12 for 129'
brewery = 'Beer Bazaar'


def scrape_beer_bazaar():
    print("------------------------------------------ in beer bazaar file")
    results = []
    supplier = brewery

    # First delete existing beers, then scrape and add the new ones
    #Beer.query.filter(Beer.supplier == 'Beer Bazaar').delete()
    #db.session.commit() 

    html = urlopen(base_url).read()
    soup = BeautifulSoup(html, features="html.parser")
    script = soup.find('script', id='bundle-builder-app--bundle--data')
    script = str(script)[506:]
    beers = parse_js_object(script)

    for beer in beers:

        # Name
        name = beer['handle']
        print(name)

        # Image
        img = beer['image']['src']
        print(img)

        print('\n')


        new_beer = [name, price, base_url, img, supplier, brewery]
        results.append(new_beer)

        #results.append(json.dumps(new_beer.__dict__))

        #db.session.add(new_beer)  
        #db.session.commit() 
        
        #print(results)    
    return results
    print(f"Finished scraping: {supplier}!")