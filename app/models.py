from app import db

class Features(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    demise_place = db.Column(db.String)
    demise_date = db.Column(db.Date)
    age = db.Column(db.Integer)