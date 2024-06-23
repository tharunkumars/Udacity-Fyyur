#----------------------------------------------------------------------------#
################ Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel

# Update from Tharun, Incorporating Review Comments on PEP8 Starts
#from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask import (
  Flask, 
  render_template, 
  request, 
  Response, 
  flash, 
  redirect, 
  url_for
)
## Incorporating Review Comments on PEP8 Ends

from jinja2.utils import markupsafe
from flask_sqlalchemy import SQLAlchemy
#Update from Tharun
from flask_migrate import Migrate
import logging
from logging import Formatter, FileHandler
from flask_wtf import *
#from forms import *

# Update from Tharun, Incorporating Review Comments on refactoring models STARTS
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from models import *
from forms import * 
from flask import app
# Update from Tharun, Incorporating Review Comments on refactoring models Ends

#----------------------------------------------------------------------------#
################ App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')

# Update from Tharun, Incorporating Review Comments on refactoring models STARTS
#db = SQLAlchemy(app)
db.init_app(app)
# moment = Moment(app)
# Update from Tharun, Incorporating Review Comments on refactoring models Ends
# Update from Tharun
migrate = Migrate(app, db)

# TODO: connect to a local postgresql database
# Update from Tharun, Connection Establised using the 
# config params in config.py class

#----------------------------------------------------------------------------#
################ Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
################ Controllers.
#----------------------------------------------------------------------------#

#  ----------------------------------------------------------------
################  Controllers Home Page
#  ----------------------------------------------------------------
@app.route('/')
def index():
  # Update from Tharun, Leaving the create_all() function as is, 
  # as this will not cause any Change to an existing table
  print(" Inside the main Route ")
  # Update from Tharun,Commenting the below block to avoid 
  # any new record entries into tables
  """
  db.create_all()
  """
  return render_template('pages/home.html')

#  ----------------------------------------------------------------
################  Controllers Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  # TODO: replace with real venues data.
  #       num_upcoming_shows should be aggregated based on number of upcoming shows per venue.
  # Update from Tharun, Including Code for Venue Details Retrival from DB.

  """
    formedquery = db.session.query(Venue)
    data = formedquery.group_by(Venue.id,Venue.state).order_by(Venue.city).all()

    for venueV in data:
      print("Venue Details   " + venueV.name)
  """
  # Update from tharun, incorporating review comments 
  # Including logic for retrival from DB, Review Comments
  data = VenueModel.query.all()
  return render_template('pages/venues.html', areas=data);

@app.route('/venues/search', methods=['POST'])
def search_venues():
  # TODO: implement search on venues with partial string search. 
  # Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
  """
  response={
    "count": 1,
    "data": [{
      "id": 2,
      "name": "The Dueling Pianos Bar",
      "num_upcoming_shows": 0,
    }]
  }
  # Update from Tharun, Including Code for Venue Details Retrival
  #  from DB based on string pattern
  
  print ( " ####### venueID ##### " + searchTermValue)
  formedquery = db.session.query(Venue)
  response = formedquery.filter(Venue.name.ilike("%"+searchTermValue+"%")).all()
  """
  # Update from tharun, incorporating review comments 
  # Including logic for retrival from DB, Review Comments
  searchTermValue =  request.form.get('search_term') 
  print ( " ####### searchTermValue ##### " + searchTermValue)
  formedquery = db.session.query(VenueModel)
  data = formedquery.filter(VenueModel.name.ilike("%"+searchTermValue+"%")).all()
  dataCount = len(data)
  print(" dataCount " )
  for venueV in data:
    print("Venue Details   " + venueV.name)
    print( venueV.id)
    print("Venue Details   " + venueV.address)
  return render_template('pages/search_venues.html', dataCount=dataCount, data=data, search_term=request.form.get('search_term', ''))

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
  """
  
  """
  # Update from Tharun, didnot find time to change the UI 
  # however on hitting the URL directly with right Venue id 
  # we get the desired results 
  # ex :  http://127.0.0.1:5000/venues/1
  print( "  venue_id   :  " , venue_id)
  venueV = Venue.query.filter_by(id=venue_id).first()
  return render_template('pages/show_venue.html', venue=venueV)

#----------------------------------------------------------------------------#
################  Create Venue
#  --------------------------------------------------------------------------#

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
  # updates from Tharun
  form = VenueGetForm()  
  objVenue = Venue()
  ## Update from Tharun, invoking additional Custom Validator methods via validate_on_submit methods
  form.validate_on_submit()
  form.populate_obj(objVenue)
  print ( " ####### venueID ##### " + objVenue.name)
  db.session.add(objVenue)  
  db.session.commit()
  # on successful db insert, flash success
  flash('Venue ' + request.form['name'] + ' was successfully listed!  ')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.

  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
  return None

#  ----------------------------------------------------------------  
################  Artists Functionality
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database
  """data=[{
    "id": 4,
    "name": "Guns N Petals",
  }, {
    "id": 5,
    "name": "Matt Quevedo",
  }, {
    "id": 6,
    "name": "The Wild Sax Band",
  }]
  """

  formedquery = db.session.query(Artist)
  data = formedquery.group_by(Artist.id,Artist.state).order_by(Artist.city).all()
  #data = formedquery
  #data = Venue.query.all()
  for artistV in data:
    print("Venue Details   " + artistV.name)
  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".
  response={
    "count": 1,
    "data": [{
      "id": 4,
      "name": "Guns N Petals",
      "num_upcoming_shows": 0,
    }]
  }
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
 
  # Update from Tharun, didnot find time to change the UI 
  # however on hitting the URL directly with right Arist id 
  # we get the desired results 
  # ex :  http://127.0.0.1:5000/artists/1
  print( "  artist_id   :  " , artist_id)
  artistV = Artist.query.filter_by(id=artist_id).first()
  return render_template('pages/show_artist.html', artist=artistV)

#  ----------------------------------------------------------------
################  Update Individual Artist
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  artist={
    "id": 4,
    "name": "Guns N Petals",
    "genres": ["Rock n Roll"],
    "city": "San Francisco",
    "state": "CA",
    "phone": "326-123-5000",
    "website": "https://www.gunsnpetalsband.com",
    "facebook_link": "https://www.facebook.com/GunsNPetals",
    "seeking_venue": True,
    "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
    "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"
  }
  # TODO: populate form with fields from artist with ID <artist_id>
  # Update from Tharun, Could not find time update single artist, though the logic is same
  # retrieve the Artist from DB based on the id from form 
  # update with new values
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes

  # Update from Tharun, Could not find time update single artist, though the logic is same
  # retrieve the Artist from DB based on the id from form 
  # update with new values
  return redirect(url_for('show_artist', artist_id=artist_id))

#  ----------------------------------------------------------------
################  Update Individual Venue
#  ----------------------------------------------------------------

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  venue={
    "id": 1,
    "name": "The Musical Hop",
    "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
    "address": "1015 Folsom Street",
    "city": "San Francisco",
    "state": "CA",
    "phone": "123-123-1234",
    "website": "https://www.themusicalhop.com",
    "facebook_link": "https://www.facebook.com/TheMusicalHop",
    "seeking_talent": True,
    "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
    "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"
  }
  # TODO: populate form with values from venue with ID <venue_id>
  # Update from Tharun, Could not find time update single venue, though the logic is same
  # retrieve the venue from DB based on the id from form 
  # update with new values
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  # Update from Tharun, Could not find time update single venue, though the logic is same
  # retrieve the venue from DB based on the id from form 
  # update with new values
  return redirect(url_for('show_venue', venue_id=venue_id))

#  ----------------------------------------------------------------
################  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion

  # Update from Tharun, Creation of new Artist
  form = ArtistGetForm()  
  objArtist = Artist()
  form.populate_obj(objArtist)
  print ( " ####### venueID ##### " + objArtist.name)
  db.session.add(objArtist)  
  db.session.commit()
  # on successful db insert, flash success
  flash('Artist ' + request.form['name'] + ' was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # Update from Tharun, Negative scenario unable to implement due to time constraints
  # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
  return render_template('pages/home.html')

#  ----------------------------------------------------------------  
################  Shows Functionality
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.

  ### Update from Tharun, Retrieving Values from DB and showing in UI
  print("INSIDE SHOWS search")
  formedquery = db.session.query(shows)
  data = formedquery.group_by(shows.venue_id).all()
  for showsV in data:
    print("Venue Details   " + showsV.venue_id)
  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create', methods=['GET'])
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead

  # updates from Tharun
  # Retriev the VenueId and ArtistID from the form

  input_Venue_id = request.form.get('venue_id')
  input_Artist_id = request.form.get('artist_id')  

  # Retriev the records for Venue and Artist
  venueV = db.session.query(Venue).filter_by(id=input_Venue_id).first()
  artistV = db.session.query(Artist).filter_by(id=input_Artist_id).first()
  #resultVenue = Venue.query.filter_by(id=input_Venue_id)
  if venueV:
    print( " ####### venue Name ##### " + venueV.name)
    flash(' we have a venue named ' +  venueV.name)
  else:
     flash('No such Venue')

  if artistV:
    print( " ####### Artist Name ##### " + artistV.name)
    flash(' we have a venue named ' +  artistV.name)
  else:
     flash('No such Artist')

  # Poppulate Association Table Shows
  venueV.artists.append(artistV)
  db.session.commit()

  # on successful db insert, flash success
  flash('Show for Artist ' + artistV.name + ' was successfully listed for venue  ' + venueV.name)
  # TODO: on unsuccessful db insert, flash an error instead.
  # Update from Tharun, Negative scenario unable to implement due to time constraints
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  # """
  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
################ Application Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
#----------------------------------------------------------------------------#
# Mock Data.
#----------------------------------------------------------------------------#

## Update from Tharun :: Moved the Shows Mock Data here 
## for better readability and for reference

"""
  data=[{
    "venue_id": 1,
    "venue_name": "The Musical Hop",
    "artist_id": 4,
    "artist_name": "Guns N Petals",
    "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
    "start_time": "2019-05-21T21:30:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "artist_id": 5,
    "artist_name": "Matt Quevedo",
    "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
    "start_time": "2019-06-15T23:00:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-01T20:00:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-08T20:00:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-15T20:00:00.000Z"
  }]
"""

## Update from Tharun :: Moved the Displays Individual Dummy Artist Data here 
## for better readability and for reference
"""
@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):

  # shows the artist page with the given artist_id
  # TODO: replace with real artist data from the artist table, using artist_id

  data1={
    "id": 4,
    "name": "Guns N Petals",
    "genres": ["Rock n Roll"],
    "city": "San Francisco",
    "state": "CA",
    "phone": "326-123-5000",
    "website": "https://www.gunsnpetalsband.com",
    "facebook_link": "https://www.facebook.com/GunsNPetals",
    "seeking_venue": True,
    "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
    "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
    "past_shows": [{
      "venue_id": 1,
      "venue_name": "The Musical Hop",
      "venue_image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
      "start_time": "2019-05-21T21:30:00.000Z"
    }],
    "upcoming_shows": [],
    "past_shows_count": 1,
    "upcoming_shows_count": 0,
  }
  data2={
    "id": 5,
    "name": "Matt Quevedo",
    "genres": ["Jazz"],
    "city": "New York",
    "state": "NY",
    "phone": "300-400-5000",
    "facebook_link": "https://www.facebook.com/mattquevedo923251523",
    "seeking_venue": False,
    "image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
    "past_shows": [{
      "venue_id": 3,
      "venue_name": "Park Square Live Music & Coffee",
      "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
      "start_time": "2019-06-15T23:00:00.000Z"
    }],
    "upcoming_shows": [],
    "past_shows_count": 1,
    "upcoming_shows_count": 0,
  }
  data3={
    "id": 6,
    "name": "The Wild Sax Band",
    "genres": ["Jazz", "Classical"],
    "city": "San Francisco",
    "state": "CA",
    "phone": "432-325-5432",
    "seeking_venue": False,
    "image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "past_shows": [],
    "upcoming_shows": [{
      "venue_id": 3,
      "venue_name": "Park Square Live Music & Coffee",
      "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
      "start_time": "2035-04-01T20:00:00.000Z"
    }, {
      "venue_id": 3,
      "venue_name": "Park Square Live Music & Coffee",
      "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
      "start_time": "2035-04-08T20:00:00.000Z"
    }, {
      "venue_id": 3,
      "venue_name": "Park Square Live Music & Coffee",
      "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
      "start_time": "2035-04-15T20:00:00.000Z"
    }],
    "past_shows_count": 0,
    "upcoming_shows_count": 3,
  }
  data = list(filter(lambda d: d['id'] == artist_id, [data1, data2, data3]))[0]
  
"""
## Update from Tharun :: Moved the Dummy Data for Venue
## for better readability and for reference

"""
@app.route('/venues')
def venues():
data=[{
    "city": "San Francisco",
    "state": "CA",
    "venues": [{
      "id": 1,
      "name": "The Musical Hop",
      "num_upcoming_shows": 0,
    }, {
      "id": 3,
      "name": "Park Square Live Music & Coffee",
      "num_upcoming_shows": 1,
    }]
  }, {
    "city": "New York",
    "state": "NY",
    "venues": [{
      "id": 2,
      "name": "The Dueling Pianos Bar",
      "num_upcoming_shows": 0,
    }]
  }]
"""


## Update from Tharun :: Moved the Displays Individual Dummy Venue Data here 
## for better readability and for reference
"""
@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  
data1={
    "id": 1,
    "name": "The Musical Hop",
    "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
    "address": "1015 Folsom Street",
    "city": "San Francisco",
    "state": "CA",
    "phone": "123-123-1234",
    "website": "https://www.themusicalhop.com",
    "facebook_link": "https://www.facebook.com/TheMusicalHop",
    "seeking_talent": True,
    "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
    "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
    "past_shows": [{
      "artist_id": 4,
      "artist_name": "Guns N Petals",
      "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
      "start_time": "2019-05-21T21:30:00.000Z"
    }],
    "upcoming_shows": [],
    "past_shows_count": 1,
    "upcoming_shows_count": 0,
  }
  data2={
    "id": 2,
    "name": "The Dueling Pianos Bar",
    "genres": ["Classical", "R&B", "Hip-Hop"],
    "address": "335 Delancey Street",
    "city": "New York",
    "state": "NY",
    "phone": "914-003-1132",
    "website": "https://www.theduelingpianos.com",
    "facebook_link": "https://www.facebook.com/theduelingpianos",
    "seeking_talent": False,
    "image_link": "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80",
    "past_shows": [],
    "upcoming_shows": [],
    "past_shows_count": 0,
    "upcoming_shows_count": 0,
  }
  data3={
    "id": 3,
    "name": "Park Square Live Music & Coffee",
    "genres": ["Rock n Roll", "Jazz", "Classical", "Folk"],
    "address": "34 Whiskey Moore Ave",
    "city": "San Francisco",
    "state": "CA",
    "phone": "415-000-1234",
    "website": "https://www.parksquarelivemusicandcoffee.com",
    "facebook_link": "https://www.facebook.com/ParkSquareLiveMusicAndCoffee",
    "seeking_talent": False,
    "image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
    "past_shows": [{
      "artist_id": 5,
      "artist_name": "Matt Quevedo",
      "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
      "start_time": "2019-06-15T23:00:00.000Z"
    }],
    "upcoming_shows": [{
      "artist_id": 6,
      "artist_name": "The Wild Sax Band",
      "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
      "start_time": "2035-04-01T20:00:00.000Z"
    }, {
      "artist_id": 6,
      "artist_name": "The Wild Sax Band",
      "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
      "start_time": "2035-04-08T20:00:00.000Z"
    }, {
      "artist_id": 6,
      "artist_name": "The Wild Sax Band",
      "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
      "start_time": "2035-04-15T20:00:00.000Z"
    }],
    "past_shows_count": 1,
    "upcoming_shows_count": 1,
  }
  data = list(filter(lambda d: d['id'] == venue_id, [data1, data2, data3]))[0]
"""
## Update from Tharun :: Moved the BootStrap Data Creation for Venue and Artist here 
## for better readability and for reference
# below direct update of records WAS done for bootstrapping the application and 
# using it for testing purposes
"""
  #Create object for Venue and adding Values into the table
  Venue1 = Venue(id = 4,
                 name= "The Musical Hop",
                 city = "San Francisco 1",
                 state = "CA", 
                 address = "AddressVenue1 1015 Folsom Street",
                 phone = "123-123-1234",
                 facebook_link = "https://www.facebook.com/TheMusicalHop",
                 image_link = "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
                 website_link = "https://www.themusicalhop.com",
                 lookingForTalent = True,
                 descForTalent = "Venue1Talent"
                )
  Venue2 = Venue(id = 5,
                 name="The Dueling Pianos Bar",
                 city = "New York 1",
                 state = "NY",
                 address = "AddressVenue2 1024 Folsom Street",
                 phone = "123-123-1234",
                 facebook_link =   "https://www.facebook.com/TheDuelingPianosBar",
                 image_link =    "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
                 website_link =    "https://www.theDuelingPianosBar.com",
                 lookingForTalent =    True,
                 descForTalent = "Venue2Talent"
                    )
  Venue3 = Venue(id = 6,
                 name="Park Square Live Music & Coffee",
                 city = "San Francisco 2",
                 state ="CA",
                 address = "AddressVenue3 1006 Folsom Street",
                 phone = "123-123-1234",
                 facebook_link =    "https://www.facebook.com/ParkSquareLiveMusicCoffee",
                 image_link =     "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
                 website_link =      "https://www.theParkSquareLiveMusicCoffee.com",
                 lookingForTalent =     True,
                 descForTalent = "Venue3Talent"
                  )
  
  VenueList = [Venue1,Venue2,Venue3]
  db.session.add_all(VenueList)
 
  Artist1 = Artist(id = 4,
                   name="The Musical Hop",
                   city = "San Francisco 1 ",
                   state ="CA",
                   address = "AddressVenue1 1015 Folsom Street",
                   phone = "123-123-1234",
                   facebook_link =   "https://www.facebook.com/TheMusicalHop",
                   image_link =    "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
                   website_link =   "https://www.themusicalhop.com",
                   genres =  "Jazz Reggae Swing Classical Folk",
                   lookingForVenue = True,
                   descForVenue = "Venue1Talent"
                    )
  Artist2 = Artist(id = 5,
                   name="The Dueling Pianos Bar",
                   city = "New York 4 ",
                   state ="NY",
                   address = "AddressVenue2 1024 Folsom Street",
                   phone = "123-123-1234",
                   facebook_link =   "https://www.facebook.com/TheDuelingPianosBar",
                   image_link =    "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
                   website_link =   "https://www.theDuelingPianosBar.com",
                   genres =  "Classical R&B Hip-Hop",
                   lookingForVenue = True,
                   descForVenue = "Venue2Talent"
                    )
  Artist3 = Artist(id = 6,
                   name="Park Square Live Music & Coffee",
                   city = "San Francisco 5 ",
                   state ="CA",
                   address = "AddressVenue3 1006 Folsom Street",
                   phone = "123-123-1234",
                   facebook_link =   "https://www.facebook.com/ParkSquareLiveMusicCoffee",
                   image_link =    "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
                   website_link =   "https://www.theParkSquareLiveMusicCoffee.com",
                   genres =  "RocknRoll Jazz Classical Folk",
                   lookingForVenue = True,
                   descForVenue = "Venue3Talent"
                    )
  ArtistList = [Artist1,Artist2,Artist3]
  db.session.add_all(ArtistList)
  
  db.session.commit()
  """