from app import db

class Artifact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    set_key = db.Column(db.String(50), nullable=False)
    slot_key = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    rarity = db.Column(db.Integer, nullable=False)
    main_stat_key = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    lock = db.Column(db.Boolean, default=False)

    # Relationship with the Substat model
    substats = db.relationship('Substat', backref='artifact', lazy=True, cascade='all, delete-orphan')

class Substat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    
    # Foreign key to relate each substat to an artifact
    artifact_id = db.Column(db.Integer, db.ForeignKey('artifact.id'), nullable=False)
