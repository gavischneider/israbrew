from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////beers.db'

#db.init_app(app)
#db.create_all()

db = SQLAlchemy()


app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')

db.init_app(app)

with app.app_context():
    from israbrew import routes # Import routes
    db.create_all()  # Create sql tables for our data models
