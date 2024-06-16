from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask import current_app

from flask_migrate import Migrate

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from App!!"

if __name__ == '__main__':
   app.run(host="127.0.0.1" )

## FLASK_APP="app.py" FLASK_DEBUG="true" flask run