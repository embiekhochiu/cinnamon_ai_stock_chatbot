from . import db
from datetime import datetime

class UserInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(500), nullable=False)
    response = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
