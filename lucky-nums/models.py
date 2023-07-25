from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    """Connect this db to provided Lucky app"""
    db.app = app
    db.init_app(app)


"""Models for Lucky."""


class LuckyNum(db.Model):

    __tablename__ = 'luckyNums'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    birthYear = db.Column(db.Integer, nullable=False)
    email = db.Column(db.Text, default=False, unique=True)
    color = db.Column(db.Text, nullable=False)

    