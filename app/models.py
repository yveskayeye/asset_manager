from email.policy import default
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # @property
    # def password(self):
    #     raise AttributeError("password is not a readable attribute")

    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User %r>' % self.email


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Asset(db.Model):

    __tablename__ = "assets"

    asset_tag = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(80), unique=True, nullable=False)
    item_discription = db.Column(db.String(80), unique=True, nullable=False)
    condition = db.Column(db.String(80), unique=True, nullable=False)
    serial = db.Column(db.String(80), unique=True, nullable=False)
    date_manufactured = db.Column(db.String(80), unique=True, nullable=False)
    cost = db.Column(db.String(80), unique=True, nullable=False)
    purchase_date = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name
