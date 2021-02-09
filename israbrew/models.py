from flask_sqlalchemy import SQLAlchemy
import os
import sys
from israbrew import app
from . import db

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////beers.db'
#db = SQLAlchemy(app)
#db = SQLAlchemy(app)

# (db.Model):
class Beer(): 
    # id = db.Column(db.Integer, primary_key = True)
    # name = db.Column(db.String(120), nullable=False)
    # brewery = db.Column(db.String(120))
    # price = db.Column(db.String(60))
    # url = db.Column(db.String(250), nullable=False)
    # image = db.Column(db.String(250), nullable=False)

    def __init__(self, name, price, url, image, brewery=""):
        self.name = name
        self.brewery = brewery
        self.price = price
        self.url = url
        self.image = image
