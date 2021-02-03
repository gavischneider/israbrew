from israbrew import app
from israbrew.beer_and_beyond import scrape_beer_and_beyond
from israbrew.biratenu import scrape_biratenu
from israbrew.mendelson_heshin import scrape_mendelson_heshin
import json

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/beer')
def test():
    beers = scrape_beer_and_beyond()
    return {'beers': beers}