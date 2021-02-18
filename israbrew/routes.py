from flask import current_app as app, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from israbrew.beer_and_beyond import scrape_beer_and_beyond
from israbrew.biratenu import scrape_biratenu
from israbrew.mendelson_heshin import scrape_mendelson_heshin
from israbrew.beerz import scrape_beerz
from israbrew.beer_bazaar import scrape_beer_bazaar
from israbrew.keshet_teamim import scrape_keshet_teamim
from israbrew.tiv_taam import scrape_tiv_taam
from .models import Beer, BeerSchema
from israbrew import db
import datetime
import time
import json
import time
import atexit

@app.route('/api')
def hello():
    return 'Welocome to IsraBrew!'

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
    
def scrape_one(scrape_func, supplier):
    # Delete all beers by the supplier before adding the new ones
    Beer.query.filter_by(supplier=supplier).delete()
    db.session.commit() 

    b = scrape_func()
    print(f"Starting to add beers from {b[0][4]} to DB")
    for beer in b:
        new_beer = Beer(beer[0], beer[1], beer[2], beer[3], beer[4], beer[5])
        db.session.add(new_beer)  
        db.session.commit() 
    print(f"Finished addiing beers from {b[0][4]} to DB")

def scrape_all():
    year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())
    print(f'Scraping now at: {hour}:{min}, {month}/{day}/{year}')
    print(f'I will scrape beers next at: {hour + 6}:{min}, {month}/{day}/{year}')

    scrape_one(scrape_beer_and_beyond, 'Beer And Beyond')
    scrape_one(scrape_biratenu, 'Biratenu')
    scrape_one(scrape_mendelson_heshin, 'Mendelson Heshin')
    scrape_one(scrape_beerz, 'BeerZ')
    scrape_one(scrape_beer_bazaar, 'Beer Bazaar')
    scrape_one(scrape_keshet_teamim, 'Keshet Teamim')
    scrape_one(scrape_tiv_taam, 'Tiv Taam')
    print('Finished scraping...')

# Call scrape_all once, then create a scheduler that runs scrape_all every 43200 seconds / 12 hours 
#scrape_all()
#scheduler = BackgroundScheduler()
#scheduler.add_job(func=scrape_all, trigger="interval", seconds=43200)
#scheduler.start()

# Shut down the scheduler when exiting the app
#atexit.register(lambda: scheduler.shutdown())