import os
from flask import Flask, request # importera Flask-appen
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def test():
    ret = { 
        'msg': 'Flask works on Rahti!', 
        'env': os.environ.get('ENV_VAR', 'Cannot find variable ENV_VAR') 
    }

    return ret


if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
