from app.ext import db
from app.core.model import Model


class Order(Model):
    id = db.Column(db.Integer, primary_key=True)
