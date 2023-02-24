from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Users(db.Model, UserMixin):
    User_id = db.Column(db.Integer, primary_key=True)
    User_name = db.Column(db.String(80), unique=False, nullable=False)
    User_surname = db.Column(db.String(80), unique=False, nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)
    Password_hash = db.Column(db.String(256), unique=False, nullable=False)
    Age = db.Column(db.Integer, unique=False, nullable=False)
    Weight = db.Column(db.Integer, unique=False, nullable=False)
    Height = db.Column(db.Integer, unique=False, nullable=False)
    Physical_activity_id = db.Column(db.Integer, db.ForeignKey('physical_activity.Physical_activity_id'),
                                     nullable=False)
    Metabolism = db.Column(db.Integer, unique=False, nullable=False)
    Gender = db.Column(db.String(1), unique=False, nullable=False)

    def get_id(self):
        return self.User_id


class Physical_activity(db.Model):
    Physical_activity_id = db.Column(db.Integer, primary_key=True)
    Physical_activity_name = db.Column(db.String(80), unique=False, nullable=False)
    Coefficient = db.Column(db.Float, unique=False, nullable=False)

    def get_id(self):
        return self.Physical_activity_id

