from flask_sqlalchemy import SQLAlchemy
import os
import sys
#from israbrew import app
#from israbrew.beer_bazaar import db
from israbrew import db, ma
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

class BeerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Beer
        #fields = ("id", name", "price", "url", "image", "supplier", "brewery")
    id = ma.auto_field()
    name = ma.auto_field()
    price = ma.auto_field()
    url = ma.auto_field()
    image = ma.auto_field()
    supplier = ma.auto_field()
    brewery = ma.auto_field()