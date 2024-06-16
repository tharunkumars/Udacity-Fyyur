from flask import Flask, render_template, jsonify, abort,  request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

# Creates a flask app __name__  dunder variable creates a app in the name of the file
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ToDo(db.Model):
    __tablename__ = 'todoapp'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f'<ToDo ID: {self.id}, description: {self.description}, completed: {self.completed}>'

@app.route('/')
def index():
    db.create_all()
    return render_template('index.html', data=ToDo.query.all())
    """return render_template
        ('index.html', data=
            [   {
                'description': 'Todo 1'
                },
                {
                'description': 'Todo 2'
                }, 
                {
                'description': 'Todo 3'
                }
            ]
        )
    """ 
# the index.html is named after the route and route handler 

if __name__ == '__main__':
   app.run(host="127.0.0.1" )