from flask_sqlalchemy import SQLAlchemy
import os
import sys
#from israbrew import app

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////beers.db'
#db = SQLAlchemy(app)

# db.Model
class Beer():
    def __init__(self, name, price, url, image, brewery=""):
        self.name = name
        self.brewery = brewery
        self.price = price
        self.url = url
        self.image = image