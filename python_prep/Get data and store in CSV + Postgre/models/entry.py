from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Database Model


class Entry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    api = db.Column(db.String(80), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    auth = db.Column(db.String(80), nullable=True)
    https = db.Column(db.Boolean, nullable=True)
    cors = db.Column(db.String(80), nullable=True)
    link = db.Column(db.String(120), nullable=True, unique=True)
    category = db.Column(db.String(80), nullable=True)

    def __init__(self,  api, description, auth, https, cors, link, category, id=None):
        self.id = id
        self.api = api
        self.description = description
        self.auth = auth
        self.https = https
        self.cors = api
        self.link = link
        self.category = category

    def __repr__(self):
        return '<Api %r>' % self.api
