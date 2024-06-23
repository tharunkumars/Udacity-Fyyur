from datetime import datetime

# Update from tharun, incorporating review comments Starts
# from flask_wtf import Form
from flask_wtf import FlaskForm as Form
# from flask_wtf import ValidationError
from wtforms.validators import ValidationError
import re
from enumsTry import enum_list_Of_Genres, enum_list_Of_States

# incorporating review comments Ends

from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL

from flask_moment import Moment
from flask import Flask
# Update from tharun, incorporating review comments Starts
app = Flask(__name__)
moment = Moment(app)

## moving commonly used State Data into common dictionary
list_Of_States = [
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
## moving commonly used Genres Data into common dictionary
list_Of_Genres = [
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
# incorporating review comments Ends

class ShowForm(Form):
    artist_id = StringField(
        'artist_id', validators=[DataRequired()]
    )
    venue_id = StringField(
        'venue_id', validators=[DataRequired()]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=
        [DataRequired()],
         choices = list_Of_States,
        # choices=list_Of_States   
        # enum_list_Of_States.choices_static()     
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices= list_Of_Genres
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    website_link = StringField(
        'website_link'
    )
    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description'
    )

class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=list_Of_States
    )
    phone = StringField(
        # TODO implement validation logic for phone 
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=list_Of_Genres 
     )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL()]
     )

    website_link = StringField(
        'website_link'
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description'
     )


# Update from tharun, incorporating review comments Starts
## including additional Custom Validator methods               
def validate_genres (self, field):
    if not set(field.data).issubset(dict (list_Of_Genres.choices()).keys()):
        raise ValidationError('Invalid Genres ')

def validate_state(self, field):
    if field.data not in dict(list_Of_States.choices()).keys(): 
        raise ValidationError('Invalid State ')

## including additional Custom Validator methods    
def validate_phone(self, field):
    if not is_valid_phoneNumber(field.data):
        raise ValidationError('Invalid phone Number')
    
##Regex Validation of input phone number
def is_valid_phoneNumber(phoneNumber):
    regexPattern = re.compile(r'^\{?([0-9]{3})?[-. ]?([0-9]{3})?[-. ]?([0-9]{4})$')
    if re.match(regexPattern, phoneNumber):
        return True
    else:
        return False


# Not using this but learnt about Key Word arguments 
# that can be used in methods in Python    
def validate(self, **kwargs):
    return super(VenueForm, self).validate(**kwargs)    

# Update from tharun, incorporating review comments Ends


"""
#----------------------------------------------------------------------------#
################ old Forms maintained for reference
#----------------------------------------------------------------------------#

class VenueGetForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  city = StringField('city', validators=[DataRequired()])
  address = StringField('address', validators=[DataRequired()])
  facebook_link = StringField('facebook_link', validators=[DataRequired()])
  image_link = StringField('image_link', validators=[DataRequired()])
  website_link = StringField('website_link', validators=[DataRequired()])
  seeking_talent = StringField('seeking_talent', validators=[DataRequired()])
  seeking_description = StringField('seeking_description', validators=[DataRequired()])
  ## Update from Tharun, invoking additional Custom Validator methods   
  phone = StringField('phone', validators=[DataRequired(),validate_phone(FlaskForm)])
  state = StringField('state', validators=[DataRequired(),validate_state(FlaskForm)])
  genres = StringField('genres', validators=[DataRequired(),validate_genres(FlaskForm)])

class ArtistGetForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  city = StringField('city', validators=[DataRequired()])  
  address = StringField('address', validators=[DataRequired()])  
  facebook_link = StringField('facebook_link', validators=[DataRequired()])
  image_link = StringField('image_link', validators=[DataRequired()])
  website_link = StringField('website_link', validators=[DataRequired()])
  seeking_venue = StringField('seeking_venue', validators=[DataRequired()])
  seeking_description = StringField('seeking_description', validators=[DataRequired()])
  ## Update from Tharun, invoking additional Custom Validator methods   
  phone = StringField('phone', validators=[DataRequired(),validate_phone])
  state = StringField('state', validators=[DataRequired(),validate_state])
  genres = StringField('genres', validators=[DataRequired(),validate_genres])

class ShowGetForm(FlaskForm):
  venue_id = StringField('venue_id', validators=[DataRequired()])
  artist_id = StringField('artist_id', validators=[DataRequired()])
  start_time = StringField('start_time', validators=[DataRequired()])
"""