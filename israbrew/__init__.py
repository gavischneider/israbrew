from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import schedule
import time
import threading
import os
import sys
from config import Config
#from israbrew.models import db
from flask_marshmallow import Marshmallow



#db = SQLAlchemy()

#def create_app():
print("CREATE APP")
app = Flask(__name__, instance_relative_config=False)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../beers.db'
app.config.from_object('config.Config')
db = SQLAlchemy(app)
ma = Marshmallow(app)

#db.init_app(app)

with app.app_context():
    from israbrew import models
    from israbrew import routes 
#     db.create_all()

    #return app
