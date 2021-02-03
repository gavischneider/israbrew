import time
from flask import Flask
import re
import os
import sys

#sys.path.append('server/models')
#import models
#from models.bandb import scrape_beer_and_beyond

app = Flask(__name__)

from israbrew import routes