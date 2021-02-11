from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_marshmallow import Marshmallow
import schedule
import time
import threading
import os
import sys

print("CREATE APP")
app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
ma = Marshmallow(app)

with app.app_context():
    from israbrew import models
    from israbrew import routes
