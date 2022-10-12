import os
from flask import request
from dotenv import load_dotenv

from flask_app import app # # importera Flask-appen
from models import User # importera User från models

load_dotenv()

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return { 
            'method': request.method,
            'msg': 'GitHub Webhook deployment works!',
            'env': os.environ.get('ENV_VAR', 'Cannot find variable ENV_VAR')
        }
        
    if request.method == 'POST':
        body = request.get_json()

        return {
            'msg': 'You POSTed something',
            'request_body': body
        }


@app.route("/users", methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = []
        for user in User.query.all():
            users.append({
                'id': user.id,
                'email': user.email,
                'updated_at': user.updated_at
            })
        return users

    if request.method == 'POST':
        body = request.get_json()
        new_user = User(email=body['email'])
        db.session.add(new_user)
        db.session.commit()
        return { 'msg': 'User created', 'id': new_user.id}        