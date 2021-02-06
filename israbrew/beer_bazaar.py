from bs4 import BeautifulSoup
#from urllib.request import urlopen
import re
from israbrew.models import Beer
import requests
from requests_html import HTMLSession, AsyncHTMLSession
import json
import aiohttp
import asyncio

#for page in range(1,14):
#{page}
base_url = f'https://beerbazaar.co.il/apps/bundles/bundle/17591'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
}

price = '8 for ₪99, 12 for ₪129'

#asession = AsyncHTMLSession()

async def scrape_beer_bazaar():
    print("------------------------------------------ in beer bazaar file")
    results = []

    try:
        response = await asession.get(base_url)
        await response.html.arender(timeout=15)
        html = response.html.html
        soup = BeautifulSoup(html, features='html.parser')
        prods = soup.find('ul', class_='bundle-builder-app--bundle--section--product-list')
        #print(prods)
        
        items = prods.find_all('li', class_='bundle-builder-app--bundle--product')
        for item in items:
            #print(item)

            # Image
            image = item.find('img', class_='bundle-builder-app--bundle--product-image').get('src')
            print(image)

            # Name
            name = item.find('h3', class_='bundle-builder-app--bundle--product-name').text
            print(name)

            # Url
            burl = 'https://beerbazaar.co.il'
            url = item.find('a', class_='bundle-builder-app--bundle--product--show-more').get('href')
            url = burl + url
            print(url)

            print('\n')

            new_beer = Beer(name, price, url, image, 'Beer Bazaar')
            results.append(json.dumps(new_beer.__dict__))
        
        print(results)    
        return results


    except requests.exceptions.RequestException as e:
        print("------------------------------------------1")
        print(e)
        return ""

#asession.run(scrape_beer_bazaar)
#asyncio.run(scrape_beer_bazaar())
#scrape_beer_bazaar()