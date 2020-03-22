from app import db

# [column.key for column in Features.__table__.columns] ==> Get the column names

class Features(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    demise_place = db.Column(db.String)
    demise_date = db.Column(db.Date)
    age = db.Column(db.Integer)
    demise_reason = db.Column(db.String)
    home_town = db.Column(db.String)
    demise_how = db.Column(db.String)