from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Users(db.Model, UserMixin):
    User_id = db.Column(db.Integer, primary_key=True)
    Program_id = db.Column(db.Integer, db.ForeignKey('programs.Program_id'), nullable=False)
    Diet_id = db.Column(db.Integer, db.ForeignKey('diets.Diet_id'), nullable=False)

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


class Methods(db.Model):
    Method_id = db.Column(db.Integer, primary_key=True)
    Method_name = db.Column(db.String(80), unique=False, nullable=False)

    def get_id(self):
        return self.Method_id


class Days(db.Model):
    Day_id = db.Column(db.Integer, primary_key=True)
    Day_count = db.Column(db.String(80), unique=False, nullable=False)

    def get_id(self):
        return self.Day_id


class Places(db.Model):
    Place_id = db.Column(db.Integer, primary_key=True)
    Place_name = db.Column(db.String(80), unique=False, nullable=False)

    def get_id(self):
        return self.Place_id


class Programs(db.Model):
    Program_id = db.Column(db.Integer, primary_key=True)
    Program_name = db.Column(db.String(80), unique=False, nullable=False)
    Method_id = db.Column(db.Integer, db.ForeignKey('methods.Method_id'), nullable=False)
    Place_id = db.Column(db.Integer, db.ForeignKey('places.Place_id'), nullable=False)
    Day_id = db.Column(db.Integer, db.ForeignKey('days.Day_id'), nullable=False)

    def get_id(self):
        return self.Program_id


class Exercises(db.Model):
    Exercise_id = db.Column(db.Integer, primary_key=True)
    Exercise_name = db.Column(db.String(80), unique=False, nullable=False)
    Number_of_approaches = db.Column(db.Integer, unique=False, nullable=False)
    Number_of_repetitions = db.Column(db.Integer, unique=False, nullable=False)

    def get_id(self):
        return self.Exercise_id


class Exercises_programs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.Exercise_id'), nullable=False)
    Program_id = db.Column(db.Integer, db.ForeignKey('programs.Program_id'), nullable=False)

    def get_id(self):
        return self.Exercise_id


class Diets(db.Model):
    Diet_id = db.Column(db.Integer, primary_key=True)
    Diet_name = db.Column(db.String(50), nullable=False)
    Diet_calories = db.Column(db.Integer, nullable=False)
    Diet_proteins = db.Column(db.Integer, nullable=False)
    Diet_fats = db.Column(db.Integer, nullable=False)
    Diet_carbohydrates = db.Column(db.Integer, nullable=False)

    def get_id(self):
        return self.Diet_id


class Products(db.Model):
    Product_id = db.Column(db.Integer, primary_key=True)
    Product_name = db.Column(db.String(255), nullable=False, unique=True)
    Product_calories = db.Column(db.Integer, nullable=False)
    Product_proteins = db.Column(db.Integer, nullable=False)
    Product_fats = db.Column(db.Integer, nullable=False)
    Product_carbohydrates = db.Column(db.Integer, nullable=False)

    def get_id(self):
        return self.Product_id


class ProductsDiets(db.Model):
    Product_id = db.Column(db.Integer, db.ForeignKey('products.Product_id'), primary_key=True)
    Diet_id = db.Column(db.Integer, db.ForeignKey('diets.Diet_id'), primary_key=True)
    Product_weight = db.Column(db.Integer, nullable=False)

    def get_id(self):
        return self.Product_id
