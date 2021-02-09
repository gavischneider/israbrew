from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import schedule
import time
import threading
import os
import sys
#from . import beer_and_beyond, biratenu, mendelson_heshin, beerz, beer_bazaar, keshet_teamim, tiv_taam

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////beers.db'

db = SQLAlchemy()

def create_app():
    print("CREATE APP")
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        from israbrew import routes 
        db.create_all()

        return app

# class Beer(db.Model): 
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(120), nullable=False)
#     price = db.Column(db.String(60))
#     url = db.Column(db.String(250), nullable=False)
#     image = db.Column(db.String(250), nullable=False)
#     supplier = db.Column(db.String(75), nullable=False)
#     brewery = db.Column(db.String(120))

#     def __init__(self, name, price, url, image, supplier, brewery=""):
#         self.name = name
#         self.price = price
#         self.url = url
#         self.image = image
#         self.supplier = supplier
#         self.brewery = brewery

# def scrape_all():
#     #db.session.query_property(Beer).delete()
#     #Beer.query.filter().delete()
#     Beer.query.delete()
#     db.session.commit() 
#     b = scrape_beer_and_beyond()
#     b2 = scrape_biratenu()
#     b3 = scrape_mendelson_heshin()
#     b4 = scrape_beerz()
#     b5 = scrape_beer_bazaar()
#     b6 = scrape_keshet_teamim()
#     b7 = scrape_tiv_taam()
#     beers_groups = [b, b2, b3, b4, b5, b6, b7]
#     for group in beers_groups:
#         for beer in group:
#             new_beer = Beer(beer[0], beer[1], beer[2], beer[3], beer[4], beer[5])
#             db.session.add(new_beer)  
#             db.session.commit() 
 
# def myApiCall(): 
#     scrape_all()
#     # call myApi() again in 21600 seconds / 6 hours 
#     threading.Timer(21600, myApiCall).start() 
 
# myApiCall() 



