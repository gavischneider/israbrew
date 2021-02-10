from flask_sqlalchemy import SQLAlchemy
import os
import sys
#from israbrew import app
#from israbrew.beer_bazaar import db
from israbrew import db
#db = SQLAlchemy()

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////beers.db'
#db = SQLAlchemy(app)

# (db.Model):
class Beer(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.String(60))
    url = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(250), nullable=False)
    supplier = db.Column(db.String(75), nullable=False)
    brewery = db.Column(db.String(120))

    def __init__(self, name, price, url, image, supplier, brewery=""):
        self.name = name
        self.price = price
        self.url = url
        self.image = image
        self.supplier = supplier
        self.brewery = brewery