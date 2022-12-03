from app.ext import db


class Model(db.Model):
    """ Model Base """
    __abstract__ = True
