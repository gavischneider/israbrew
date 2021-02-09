from israbrew import app
from israbrew.beer_and_beyond import scrape_beer_and_beyond
from israbrew.biratenu import scrape_biratenu
from israbrew.mendelson_heshin import scrape_mendelson_heshin
from israbrew.beerz import scrape_beerz
from israbrew.beer_bazaar import scrape_beer_bazaar
import json
import asyncio
import aiohttp
from requests_html import HTMLSession, AsyncHTMLSession

beers = {};

@app.route('/api')
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
    beers['beerandbeyond'] = b
    beers['biratenu'] = b2
    beers['mendelson'] = b3
    beers['beerz'] = b4
    beers['beerbazaar'] = b5
    return {'beers': beers}