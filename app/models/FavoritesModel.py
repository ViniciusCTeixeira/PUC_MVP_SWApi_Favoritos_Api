from datetime import datetime
from app import db
import pytz


brazil_tz = pytz.timezone('America/Sao_Paulo')

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    created = db.Column(db.String, nullable=False, default=datetime.now(brazil_tz).strftime('%Y-%m-%d %H:%M:%S'))
    modified = db.Column(db.String, nullable=False, default=datetime.now(brazil_tz).strftime('%Y-%m-%d %H:%M:%S'))
    username = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    swapi_id = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)

    def __init__(self, username, description, swapi_id, type):
        self.username = username
        self.created = datetime.now(brazil_tz).strftime('%Y-%m-%d %H:%M:%S') if not self.created else self.created
        self.created = datetime.now(brazil_tz).strftime('%Y-%m-%d %H:%M:%S') if not self.created else self.created
        self.description = description
        self.swapi_id = swapi_id
        self.type = type

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.modified = datetime.now(brazil_tz).strftime('%Y-%m-%d %H:%M:%S')
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
