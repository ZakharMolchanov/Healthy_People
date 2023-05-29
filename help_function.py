from my_classes import Diets, Products, ProductsDiets  # Импортируйте соответствующие классы из модуля models
from flask_sqlalchemy import SQLAlchemy  # Импортируйте модуль SQLAlchemy для объекта db.session

# Если вы используете SQLAlchemy для работы с базой данных
db = SQLAlchemy()  # Создайте объект SQLAlchemy

# При необходимости импортируйте другие модули, которые используются в ваших функциях
from sqlalchemy import func  # Импортируйте func из sqlalchemy, если он используется в функции get_diet


def calculate_metabolism(weight, height, age, physical_activity, data):
    if data['gender'] == 'female':
        return int((65 + (9.6 * int(weight)) + (1.8 * int(height)) - (4.7 * int(age))) * float(physical_activity))
    else:
        return int((66 + (13.7 * int(weight)) + (5 * int(height)) - (6.8 * int(age))) * float(physical_activity))


def get_physical_activity_id(physical_activity):
    if physical_activity == '1':
        return 1
    elif physical_activity == '1.2':
        return 2
    elif physical_activity == '1.375':
        return 3
    elif physical_activity == '1.55':
        return 4
    elif physical_activity == '1.6375':
        return 5


def calculate_macros(metabolism):
    proteins = int((metabolism * 0.45) // 4)
    fats = int((metabolism * 0.2) // 9)
    carbs = int((metabolism * 0.35) // 4)
    return proteins, fats, carbs


def get_diet(metabolism):
    return Diets.query.order_by(func.abs(Diets.Diet_calories - metabolism)).first()


def get_diet_products(diet_id):
    products = Products.query.join(ProductsDiets).filter(ProductsDiets.Diet_id == diet_id).all()
    weights = ProductsDiets.query.filter(ProductsDiets.Diet_id == diet_id).all()

    for i in range(len(products)):
        products[i].weight = weights[i].Product_weight
    for i in range(len(products)):
        products[i].Product_proteins = int(products[i].Product_proteins * products[i].weight / 100)
        products[i].Product_fats = int(products[i].Product_fats * products[i].weight / 100)
        products[i].Product_carbohydrates = int(products[i].Product_carbohydrates * products[i].weight / 100)
        products[i].Product_calories = int(products[i].Product_calories * products[i].weight / 100)

    return products
