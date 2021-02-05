"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
from datetime import datetime

# Creates a model called `Guest` with the following fields:
# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.Integer, nullable= False)
    events_attending = db.relationship('Event', secondary='guest_event_table', back_populates='guests')



# Creates a model called `Event` with the following fields:
# - id: primary key
# - title: String column
# - description: String column
# - date_and_time: DateTime column
# - guests: relationship to "Guest" table with a secondary table

# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    date_and_time = db.Column(db.DateTime, nullable = False, default = datetime.strftime(datetime.today(), "%b %d %Y"))
    guests = db.relationship('Guest', secondary='guest_event_table', back_populates='events_attending')



#   Creates a table `guest_event_table` with the following columns:
# - guest_id: Integer column (foreign key)
# - event_id: Integer column (foreign key)



guest_event_table = db.Table('guest_event_table',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)