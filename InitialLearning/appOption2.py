from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from App using Option2!!"

if __name__ == '__main__':
   app.run(host="127.0.0.1" )

## appOption2.py