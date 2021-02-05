from israbrew import app
from israbrew.beer_and_beyond import scrape_beer_and_beyond
from israbrew.biratenu import scrape_biratenu
from israbrew.mendelson_heshin import scrape_mendelson_heshin
import json
import time

@app.route('/api')
def hello():
    return 'Hello, World!'

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/api/beer')
def scrape():
    beers = {}
    b = scrape_beer_and_beyond()
    b2 = scrape_biratenu()
    b3 = scrape_mendelson_heshin()
    beers['beerandbeyond'] = b
    beers['biratenu'] = b2
    beers['mendelson'] = b3
    return {'beers': beers}