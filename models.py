from enum import unique

from flask_login import LoginManager, UserMixin
from ext import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash



class Reg(db.Model, UserMixin) :

    __tablename__ ="Regs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    birthday = db.Column(db.Date)
    gender = db.Column(db.String)
    country = db.Column(db.String)
    role =  db.Column(db.String)

    def __init__(self, name, password, birthday, gender, country, role = "guest"):
        self.name = name
        self.password = generate_password_hash(password)
        self.birthday = birthday
        self.gender = gender
        self.country = country
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login_manager.user_loader
def load_user(user_id) :
    return Reg.query.get(user_id)


class Card(db.Model, UserMixin) :

    __tablename__ ="Cards"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    img = db.Column(db.String())
    link = db.Column(db.String())


class AddCard(db.Model, UserMixin) :

    __tablename__ ="Add_Cards"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    part = db.Column(db.String())
    img = db.Column(db.String())
