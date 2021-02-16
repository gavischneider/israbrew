from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json

def scrape_mendelson_heshin():
    results = []
    #results = 0
    base_url = f'https://mendelson-heshin.com/product-category/%d7%91%d7%99%d7%a8%d7%95%d7%aa/page/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
    }
    supplier = 'Mendelson Heshin'
    brewery = ""

    # Check how many pages there are
    html = urlopen(base_url + '1').read()
    soup = BeautifulSoup(html, features='html.parser')
    pages = int(soup.find_all('a', class_='page-numbers')[-2].text)
    print(pages)

    for page in range(1, pages + 1):
    
        html = urlopen(base_url + str(page)).read()
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
            print(link_data)
            if link_data != None:
                url = link_data.get('href')

                img = link_data.find('img').get('data-src')
                #print(img)
            else:
                url = " "
                img = " "
            
            #print(link)
            #print('\n')

            # 3. Name
            name_data = data[2]
            name = name_data.find('a').text

            # 4. Price
            price_data = data[3]

            # ------------------------------------
            price = price_data.find('bdi').text
            price = price[0] + " " + price[1:]
            #-------------------------------------
            #print(price)

            new_beer = [name, price, url, img, supplier, brewery]
            results.append(new_beer)


            #results.append(json.dumps(new_beer.__dict__))

            #db.session.add(new_beer)  
            #db.session.commit()

            #results = results + 1
            #print(results)

    #print(results)    
    return results
    print(f"Finished scraping: {supplier}!")

#scrape_mendelson_heshin()