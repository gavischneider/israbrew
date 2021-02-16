from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json

def scrape_beer_and_beyond():
    results = []
    #results = 0
    supplier = 'Beer And Beyond'

    base_url = f'https://beerandbeyond.com/collections/all-beers?page='
    product_base_url = 'https://beerandbeyond.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
    }

    # Check how many pages there are
    html = urlopen(base_url + '1').read()
    soup = BeautifulSoup(html, features='html.parser')
    pages = int(soup.find_all('span', class_='page')[-1].text)
    print(pages)

    for page in range(1, pages + 1):

        html = urlopen(base_url + str(page)).read()
        soup = BeautifulSoup(html, features='html.parser')
        prods = soup.find('div', id='CollectionSection')
        beers = prods.find_all('a')

        for beer in beers:

            # 1. Get beer image
            img = beer.find_all('div', class_='grid__image-ratio')
            if(img):
                links = re.findall(r'(//cdn.shopify.com\S+)', str(img))
                img_link = links[0]
                img_link = img_link[2:]
                img = 'https://' + img_link
                #print(img)

                # 2. Get beer url
                l = beer.get('href')
                url = product_base_url + l
                #print(link)

            # Get beer data (which holds the info we need)
            data = beer.find('div', class_='grid-product__meta')
            if(data):

                # 1. Beer name
                name = data.find_all('div')[0].text
                if '-' in name:
                    newtext = name.split('-') 
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
                    newtext = name.split(' ') 
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

                # 3. Price
                price = data.find_all('div')[2].text
                if not price[0].isascii():
                    price = price[6:]
                np = price.split(" ")
                price = np[::-1]
                # Take the NIS symbol only
                print(price)

                # If the array is longer than 2, take the whole thing to 
                if(len(price) == 2):
                    price[0] = price[0][0]
                    price = " ".join(price)
                else:
                    price = " ".join(price)

                new_beer = [name, price, url, img, supplier, brewery]
                results.append(new_beer)

                #results.append(json.dumps(new_beer.__dict__))


                #results = results + 1
                #print(results)

                #db.session.add(new_beer)  
                #db.session.commit() 

    #print(results)    
    return results
    print(f"Finished scraping: {supplier}!")

#scrape_beer_and_beyond()