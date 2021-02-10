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
from israbrew import db

#beers = {};

@app.route('/')
def hello():
    return 'Hello, World!'

# @app.route('/api/beer')
# def scrape():
#     beers = {}
#     b = scrape_beer_and_beyond()
#     b2 = scrape_biratenu()
#     b3 = scrape_mendelson_heshin()
#     b4 = scrape_beerz()
#     b5 = scrape_beer_bazaar()
#     b6 = scrape_keshet_teamim()
#     b7 = scrape_tiv_taam()
#     beers['beerandbeyond'] = b
#     beers['biratenu'] = b2
#     beers['mendelson'] = b3
#     beers['beerz'] = b4
#     beers['beerbazaar'] = b5
#     beers['keshetteamim'] = b6
#     beers['tivtaam'] = b7
#     return {'beers': beers}


def scrape_all():
    #db.session.query_property(Beer).delete()
    #Beer.query.filter().delete()


    #Beer.query.delete()
    #db.session.commit() 


    b = scrape_beer_and_beyond()
    #b2 = scrape_biratenu()
    #b3 = scrape_mendelson_heshin()
    #b4 = scrape_beerz()
    #b5 = scrape_beer_bazaar()
    #b6 = scrape_keshet_teamim()
    #b7 = scrape_tiv_taam()
    #beers_groups = [b, b2, b3, b4, b5, b6, b7]
    beers_groups = [b]
    print("Starting to add beers to DB")
    for group in beers_groups:
        for beer in group:
            new_beer = Beer(beer[0], beer[1], beer[2], beer[3], beer[4], beer[5])
            db.session.add(new_beer)  
            db.session.commit() 
        print(f"Finished adding {group} to DB")
    print("Finished adding all beers to the DB")

def myApiCall():
    print(f"Scraping beers again at {datetime.datetime.now()}")
    scrape_all()
    # call myApi() again in 21600 seconds / 6 hours 
    threading.Timer(21600, myApiCall).start() 
 
myApiCall() 
