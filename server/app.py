# Start venv: source venv/bin/activate
# Export app: export FLASK_APP=server/app

import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/time')
def get_current_time():
    return {'time': time.time()}