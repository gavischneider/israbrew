# Start venv: source venv/bin/activate
# Export app: export FLASK_APP=server/app

import time
from flask import Flask
import re
import os
import sys

sys.path.append('server/models')
import models
from models import bandb

app = Flask(__name__)


@app.route('/')
def hello():
    print(sys.path)
    return 'Hello, World!'

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/beer')
def test():
    beers = bandb.scrape_beer_and_beyond()
    return {'beers': beers}
    