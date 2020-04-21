from app import db


class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    year = db.Column(db.Integer)
    price = db.Column(db.Float(asdecimal=True))
    games = db.Column(db.Integer)
    active = db.Column(db.Boolean)


    def __init__(self, name, year, price, games, active):
        self.name = name
        self.year = year
        self.price = price
        self.games = games
        self.active = active

    def __repr__(self):
        return "Console {0}".format(self.id)
