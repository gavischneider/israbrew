from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import schedule
import time
import threading
import os
import sys
from config import Config
#from israbrew.models import db



#db = SQLAlchemy()

#def create_app():
print("CREATE APP")
app = Flask(__name__, instance_relative_config=False)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../beers.db'
app.config.from_object('config.Config')
db = SQLAlchemy(app)

#db.init_app(app)

with app.app_context():
    from israbrew import models
    from israbrew import routes 
#     db.create_all()

    #return app
