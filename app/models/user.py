from app.ext import db
from app.core.model import Model


class User(Model):
    id = db.Column(db.Integer, primary_key=True)
