
from src import db


class Events(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    asin = db.Column(db.String)
    brand = db.Column(db.String)
    id_code = db.Column(db.String)
    source = db.Column(db.String)
    stars = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)

    def __init__(self, asin, brand, id, source, stars, timestamp):
        self.asin = asin
        self.brand = brand
        self.id_code = id
        self.source = source
        self.stars = stars
        self.timestamp = timestamp

    def __repr__(self):
        return f'({self.id}, {self.asin}, {self.brand}, {self.id_code}, {self.source}, {self.stars}, {self.timestamp})'

    def to_dict(self):
        return {
            'id': self.id,
            'asin': self.asin,
            'brand': self.brand,
            'id_code': self.id_code,
            'source': self.source,
            'stars': self.stars,
            'timestamp': self.timestamp.strftime('%Y-%m-%d'),
        }

