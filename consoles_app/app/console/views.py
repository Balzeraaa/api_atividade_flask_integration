import json
from flask import Blueprint, abort, jsonify
from flask_restful import Resource, reqparse
from app.console.models import Console
from app import api, db

console = Blueprint("console", __name__)

parser = reqparse.RequestParser()

parser.add_argument("name", type=str)
parser.add_argument("year", type=int)
parser.add_argument("price", type=float)
parser.add_argument("games", type=int)
parser.add_argument("active", type=bool)


@console.route("/")
@console.route("/home")
def home():
    return "Catálogo de consoles"


class ConsolesAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            consoles = Console.query.paginate(page, 10).items
            res = []
            for con in consoles:
                res.append({
                    'id': con.id,
                    'name': con.name
                })
            return jsonify(res)
        else:
            consoles = [Console.query.get(id)]
            res = {}
            for con in consoles:
                res = {
                    'id': con.id,
                    "name": con.name,
                    "year": con.year,
                    "price": con.price,
                    "games": con.games,
                    "active": con.active
                }
            return jsonify(res)
        if not consoles:
            abort(404)

    def post(self):
        args = parser.parse_args()
        name = args["name"]
        year = args["year"]
        price = args["price"]
        games = args["games"]
        active = args["active"]

        con = Console(name, year, price, games, active)
        db.session.add(con)
        db.session.commit()
        res = {"name": con.name}
        return jsonify(res)

    def delete(self, id):
        con = Console.query.get(id)
        db.session.delete(con)
        db.session.commit()
        res = {'id': id}
        return jsonify(res)

    def put(self, id):
        con = Console.query.get(id)
        args = parser.parse_args()
        name = args["name"]
        year = args["year"]
        price = args["price"]
        games = args["games"]
        active = args["active"]

        con.name = name
        con.year = year
        con.price = price
        con.games = games
        con.active = active

        db.session.commit()
        res = {'id': con.id}
        return jsonify(res)


api.add_resource(
    ConsolesAPI,
    '/api/console',
    '/api/console/<int:id>',
    '/api/console/<int:id>/<int:page>'
)
