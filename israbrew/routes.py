from israbrew import app
from israbrew.beer_and_beyond import scrape_beer_and_beyond
from israbrew.biratenu import scrape_biratenu
from israbrew.mendelson_heshin import scrape_mendelson_heshin
from israbrew.beerz import scrape_beerz
from israbrew.beer_bazaar import scrape_beer_bazaar
from israbrew.keshet_teamim import scrape_keshet_teamim
from israbrew.tiv_taam import scrape_tiv_taam

beers = {};

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/beer')
def scrape():
    beers = {}
    b = scrape_beer_and_beyond()
    b2 = scrape_biratenu()
    b3 = scrape_mendelson_heshin()
    b4 = scrape_beerz()
    b5 = scrape_beer_bazaar()
    b6 = scrape_keshet_teamim()
    b7 = scrape_tiv_taam()
    beers['beerandbeyond'] = b
    beers['biratenu'] = b2
    beers['mendelson'] = b3
    beers['beerz'] = b4
    beers['beerbazaar'] = b5
    beers['keshetteamim'] = b6
    beers['tivtaam'] = b7
    return {'beers': beers}