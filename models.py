import os

from flask_app import app # importera Flask-appen
from flask_sqlalchemy import SQLAlchemy
# load_dotenv()

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('APP_SETTINGS', 'sqlite:///db.sqlite3')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# SQLAlchemy (postgresql)
# create the extension
db = SQLAlchemy (app)

# initialize the app with the extension
db.init_app(app)

# datamodell = tabell i postgresql
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    #created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, 
        default=db.func.now(), 
        onupdate=db.func.now())

# Uncommenta dessa rader och kör en gång för att skapa tabellen
with app.app_context():
    db.create_all()