from app import db


class user(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.type
