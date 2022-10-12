import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from flask_app import app # importera Flask-appen
load_dotenv()


# SQLAlchemy (postgresql)
# create the extension
db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DB_URL')
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