from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website_link = db.Column(db.String(500))  
    genres = db.Column(db.String(120))
    #Update from Tharun to include additional fields missing from original Code  
    lookingForTalent = db.Column(db.Boolean, default=False)
    descForTalent = db.Column(db.String(500))
    # Setting BiDirectional RelationShip between Venue table (considered as Parent)
    # and Artist Table (considered as Child)
    # Shows being created as Association table
    artists = db.relationship('Artist', secondary='Shows',
      backref=db.backref('Venue', lazy=True))

# TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website_link = db.Column(db.String(500)) 
    genres = db.Column(db.String(120))
    #Update from Tharun to include additional fields missing from original Code
    lookingForVenue = db.Column(db.Boolean, default=False)
    descForVenue = db.Column(db.String(500))

# TODO: implement any missing fields, as a database migration using Flask-Migrate
     # Included in the both the Venue and Artist Models

# TODO Implement Show and Artist models, 
# and complete all model relationships and properties, as a database migration.

# Implementing a Many2Many relationship and Creating an association table in SQLAlchemy
    Shows = db.Table('Shows',
    db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id'), primary_key=True),
    db.Column('venue_name', db.String),
    db.Column('artist_id', db.Integer, db.ForeignKey('Artist.id'), primary_key=True),
    db.Column('artist_name', db.String)
    )

