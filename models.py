from app import db

class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    path = db.Column(db.String(100), nullable=False)
    downloaded = db.Column(db.Boolean, default=False, nullable=False)
