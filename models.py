import string
# from datetime import datetime
from random import choices

from .extensions import db 

const='jiimbo'

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(3), unique=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()

    def generate_short_link(self): #jiimbo as const(6)
        characters = string.digits + string.ascii_letters
        short_url =  const  + ''.join(choices(characters, k=3))               #''.join(choices(characters, k=3))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()
        
        return short_url