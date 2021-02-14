from flask import current_app as app, jsonify
from israbrew.beer_and_beyond import scrape_beer_and_beyond
from israbrew.biratenu import scrape_biratenu
from israbrew.mendelson_heshin import scrape_mendelson_heshin
from israbrew.beerz import scrape_beerz
from israbrew.beer_bazaar import scrape_beer_bazaar
from israbrew.keshet_teamim import scrape_keshet_teamim
from israbrew.tiv_taam import scrape_tiv_taam
from .models import Beer, BeerSchema
import datetime
import time
from israbrew import db
import json
import threading

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/beers')
def get_beers():
    beers = {}
    beer_schema = BeerSchema(many=True)
    b = Beer.query.filter_by(supplier='Beer And Beyond')
    output = beer_schema.dump(b)
    beers['beerandbeyond'] = output
    b2 = Beer.query.filter_by(supplier='Biratenu')
    output2 = beer_schema.dump(b2)
    beers['biratenu'] = output2
    b3 = Beer.query.filter_by(supplier='Mendelson Heshin')
    output3 = beer_schema.dump(b3)
    beers['mendelsonheshin'] = output3
    b4 = Beer.query.filter_by(supplier='BeerZ')
    output4 = beer_schema.dump(b4)
    beers['beerz'] = output4 
    b5 = Beer.query.filter_by(supplier='Beer Bazaar')
    output5 = beer_schema.dump(b5)
    beers['beerbazaar'] = output5
    b6 = Beer.query.filter_by(supplier='Keshet Teamim')
    output6 = beer_schema.dump(b6)
    beers['keshetteamim'] = output6 
    b7 = Beer.query.filter_by(supplier='Tiv Taam')
    output7 = beer_schema.dump(b7)
    beers['tivtaam'] = output7
    return {'beers': beers}
    
def scrape_one(scrape_func):

    print("In the scrape one function")

    b = scrape_func()
    print(f"Starting to add beers from {b[0][4]} to DB")
    for beer in b:
        new_beer = Beer(beer[0], beer[1], beer[2], beer[3], beer[4], beer[5])
        db.session.add(new_beer)  
        db.session.commit() 
    print(f"Finished addiing beers from {b[0][4]} to DB")

def scrape_all():

    print("In the scrape all function")

    Beer.query.filter().delete()
    db.session.commit() 

    scrape_one(scrape_beer_and_beyond)
    scrape_one(scrape_biratenu)
    scrape_one(scrape_mendelson_heshin)
    scrape_one(scrape_beerz)
    scrape_one(scrape_beer_bazaar)
    scrape_one(scrape_keshet_teamim)
    scrape_one(scrape_tiv_taam)

def myApiCall():
    #print(f"Scraping beers again at {datetime.datetime.now()}")
    year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())

    print(f'Scraping now at: {hour}:{min}, {month} {day}, {year}')
    print(f'I will scrape beers next at: {hour + 6}:{min}, {month} {day}, {year}')

    # filename = '/scrape_log.txt';
    # file = open(filename, 'a')
    # file.write(f'Scraping now at: {hour}:{min}, {month} {day}, {year}\n')
    # file.write(f'I will scrape beers next at: {hour + 6}:{min}, {month} {day}, {year}\n\n')
    # file.close()

    scrape_all()
    # call myApi() again in 21600 seconds / 6 hours 
    threading.Timer(21600, myApiCall).start() 
 
#myApiCall() 
