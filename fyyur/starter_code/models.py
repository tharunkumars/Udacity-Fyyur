from flask import (
  Flask, 
  render_template, 
  request, 
  Response, 
  flash, 
  redirect, 
  url_for,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import join,Column, String, ForeignKey
           
from sqlalchemy.orm import aliased
from flask_moment import Moment

db = SQLAlchemy()


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

# Implementing a Many2Many relationship and Creating an association 
# table in SQLAlchemy
"""
Shows = db.Table('Shows',
    db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id'), primary_key=True),
    db.Column('artist_id', db.Integer, db.ForeignKey('Artist.id'), primary_key=True)
    )
"""
class Shows_Association(db.Model):
    __tablename__ = 'Shows'

    venue_id = db.Column(ForeignKey('Venue.id'),  primary_key=True)
    artist_id = db.Column(ForeignKey('Artist.id'), primary_key=True)


class VenueModel(db.Model):
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
    genres = db.ARRAY(db.String(120))
    #Update from Tharun to include additional fields missing from original Code  
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))
    # Setting BiDirectional RelationShip between Venue table (considered as Parent)
    # and Artist Table (considered as Child)
    # Shows being created as Association table
    # artists = db.relationship('Artist', secondary='Shows',
    #  backref=db.backref('Venue', lazy=True))
    
    #Update from Tharun incorporating review comments, 
    # setting relationship between Models
    relation_Artist = db.relationship('ArtistModel',secondary='Shows',backref='Venue',viewonly=True)
    
# TODO: implement any missing fields, as a database migration using Flask-Migrate

# Creating an alias for Venue model for clarity
#venue_alias = aliased (Venue) 
class ArtistModel(db.Model):
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
    genres = db.ARRAY(db.String(120))
    #Update from Tharun to include additional fields missing from original Code
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))
    #Update from Tharun incorporating review comments, 
    # setting relationship between Models
    # Shows = db.relationship('Shows',secondary=Shows,backref='Artist')
    relation_Venue = db.relationship('VenueModel',secondary='Shows',backref='Artist',viewonly=True)
    

# TODO: implement any missing fields, as a database migration using Flask-Migrate
#Update from Tharun ,included in initial submission itself
     # Included in the both the Venue and Artist Models

# TODO Implement Show and Artist models, 
# and complete all model relationships and properties, as a database migration.

# Creating an alias for Artist model for clarity
# artist_alias = aliased (Artist) 

