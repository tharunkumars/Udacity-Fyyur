from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask import current_app

from flask_migrate import Migrate

app = Flask(__name__)
## all configuration are set in the dictionart app.config
##app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'
## DB API is optional, Can specify any specific DB APIs
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

#with app.app_context():
   

"""Declaring classes
class MyModel(db.Model) will inherit from db.Model
By inheriting from db.Model, we map from our classes to tables via SQLAlchemy ORM
Defining columns :: 
    Within our class, we declare attributes equal to db.Column(...)
    db.Column takes <datatype>, <primary_key?>, <constraint?>, <default?>
Table naming :: 
    By default, SQLAlchemy will pick the name of the table for you, 
    setting it equal to the lower-case version of your class's name. 
    Otherwise, we set the name of the table using __tablename__ = 'my_custom_table_name'.

    db.create_all() actually creates that tables based on the db.Model 
    that was configured with the associated table.
    it creates a table if its not available
    if table is allready available this wont create the table

    SQLAlchemy names the table by the name of the class, all lower cased, by default. 
    Then, if it finds a table with that name already, regardless of whether the schema matches the class,
    it will skip creating another table by that same name, and do nothing.
"""
class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=True)

    ## constrains on columns
    ## name = db.Column(db.String(), nullable=False, unique=True)
    ##
    ## Implementing a check constrain
    ## price = db.Column(db.Float, db.CheckConstraint('price>0'))
    ##
    ## Dander repr method optional, usefull during debugging
    ## def __repr__(self):
    ##    return f'<Person ID: {self.id}, name: {self.name}>'
    
@app.route('/')
def index():
    #db.create_all() This is commented during the usage of DBmigrate

    person = Person(id=4,name='Amy4',completed=False)
    db.session.add(person)
    db.session.commit()

    personObject = Person.query.filter_by(id=2)
    return "Hello " + personObject.name + " from App using SQLAlchemy !!"

    """
    Person.query.all()
    Person.query.filter_by(name='Amy')
    Person.query
    Person.query.filter_by(name='Amy').all()
    results = Person.query.filter_by(name='Amy').all()
    results[0].id
    person = Person(name='Bob 2')
    db.session.add(person)
    db.session.commit()
    Person.query()
    person1 = Person(name='New Person 1')
    person2 = Person(name='New Person 2')
    db.session.add_all([person1],[person2])
    db.session.commit()
    Person.query()
    """

if __name__ == '__main__':
   app.run(host="127.0.0.1" )