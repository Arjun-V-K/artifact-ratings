from app import db

class Artifact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    set_name = db.Column(db.String(100), nullable=False)
