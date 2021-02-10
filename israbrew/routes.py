#from israbrew import app
from flask import current_app as app
from israbrew.beer_and_beyond import scrape_beer_and_beyond
from israbrew.biratenu import scrape_biratenu
from israbrew.mendelson_heshin import scrape_mendelson_heshin
from israbrew.beerz import scrape_beerz
from israbrew.beer_bazaar import scrape_beer_bazaar
from israbrew.keshet_teamim import scrape_keshet_teamim
from israbrew.tiv_taam import scrape_tiv_taam

from .models import Beer #, db
import datetime
import time
from israbrew import db

#beers = {};

@app.route('/')
def hello():
    return 'Hello, World!'


def scrape_all():

    Beer.query.filter().delete()
    db.session.commit() 

    #beer_groups = []
    b = scrape_beer_and_beyond()
    #beer_groups.append(b)
    print("Starting to add beers from Beer And Beyond to DB")
    for beer in b:
        print(beer[0])
        new_beer = Beer(beer[0], beer[1], beer[2], beer[3], beer[4], beer[5])
        db.session.add(new_beer)  
        db.session.commit() 

    b2 = scrape_biratenu()
    #beer_groups.append(b2)
    print("Starting to add beers from Biratenu to DB")
    for beer2 in b2:
        print(beer2[0])
        new_beer2 = Beer(beer2[0], beer2[1], beer2[2], beer2[3], beer2[4], beer2[5])
        db.session.add(new_beer2)  
        db.session.commit() 

    b3 = scrape_mendelson_heshin()
    # beer_groups.append(b3)
    print("Starting to add beers from Mendelson Heshin to DB")
    for beer3 in b3:
        print(beer3[0])
        new_beer3 = Beer(beer3[0], beer3[1], beer3[2], beer3[3], beer3[4], beer3[5])
        db.session.add(new_beer3)  
        db.session.commit() 

    b4 = scrape_beerz()
    #beer_groups.append(b4)
    print("Starting to add beers from BeerZ to DB")
    for beer4 in b4:
        print(beer4[0])
        new_beer4 = Beer(beer4[0], beer4[1], beer4[2], beer4[3], beer4[4], beer4[5])
        db.session.add(new_beer4)  
        db.session.commit() 

    b5 = scrape_beer_bazaar()
    #beer_groups.append(b5)
    print("Starting to add beers from Beer Bazaar to DB")
    for beer5 in b5:
        print(beer5[0])
        new_beer5 = Beer(beer5[0], beer5[1], beer5[2], beer5[3], beer5[4], beer5[5])
        db.session.add(new_beer5)  
        db.session.commit() 

    b6 = scrape_keshet_teamim()
    #beer_groups.append(b6)
    print("Starting to add beers from Keshet Teamim to DB")
    for beer6 in b6:
        print(beer6[0])
        new_beer6 = Beer(beer6[0], beer6[1], beer6[2], beer6[3], beer6[4], beer6[5])
        db.session.add(new_beer6)  
        db.session.commit() 

    b7 = scrape_tiv_taam()
    #beer_groups.append(b7)
    print("Starting to add beers from Tiv Taam to DB")
    for beer7 in b7:
        print(beer7[0])
        new_beer7 = Beer(beer7[0], beer7[1], beer7[2], beer7[3], beer7[4], beer7[5])
        db.session.add(new_beer7)  
        db.session.commit() 

    
    ##beers_groups = [b]

    # print("Starting to add beers to DB")
    # for group in beers_groups:
    #     for beer in group:
    #         print(beer)
    #         new_beer = Beer(beer[0], beer[1], beer[2], beer[3], beer[4], beer[5])
    #         db.session.add(new_beer)  
    #         db.session.commit() 
    #     print(f'Finished adding {group} to DB')
    # print("Finished adding all beers to the DB")

def myApiCall():
    #print(f"Scraping beers again at {datetime.datetime.now()}")
    year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())
    print(f'Scraping now at: {hour}:{min}')
    print(f'I will scrape beers next at: {hour + 6}:{min}')
    scrape_all()
    # call myApi() again in 21600 seconds / 6 hours 
    threading.Timer(21600, myApiCall).start() 
 
myApiCall() 
