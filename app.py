import os
from flask_app import app # importera Flask-appen
import routes # importera routes

@app.route("/")
def test():
    ret = { 
        'msg': 'Flask works on Rahti!', 
        'cheer': os.environ.get('ENV_VAR', 'This is a test') 
    }

    return ret


if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
