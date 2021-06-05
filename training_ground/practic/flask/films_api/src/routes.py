from flask_restful import Resource, request
from typing import List 
from src import api, db
from models import *


class Smoke(Resource):
    def get(self):
        return {'message': 'OK'}, 200


class FilmListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            films = db.session.querry(Film).all()
            return [f.to_dict() for f in films], 200
        film = db.session.querry(Film).filter_by(uuid=uuid).first()
        if not film:
            return '', 404
        return film.to_dict(), 200

    def post(self):
        film_json = request.json
        if not film_json:
            return {'message': 'Wrong data'}, 400
        try:
            film = Film(
                title=film_json['title'],
                release_date=
            )        
        return create_film(film_json), 201

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass


api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)

'''curl -X POST -H "Content-Type: application/json" -d "{\"title\": \"Ready\", \"release_date\": \"2018-03-11\", \"rating\" : \"7.5\", \"lenghth\": \"140\"}" http://localhost:5000/films/'''