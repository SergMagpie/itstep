from flask_restful import Resource
from src import api, db
from src.models import Events

class Timeline(Resource):
    def get(self):

        events = list(map(lambda x: x.to_dict(), db.session.query(Events).limit(10)))
        return events, 200
