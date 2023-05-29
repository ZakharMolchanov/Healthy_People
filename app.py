from flask import Flask, request, jsonify, render_template, redirect, url_for, session, Response, send_file
from flask_login import LoginManager, login_user, login_required, current_user
from flask_bcrypt import Bcrypt
from my_classes import db, Users, Programs, Exercises, Exercises_programs, Diets, ProductsDiets, Products
from sqlalchemy import func
import io
import xlsxwriter
import pandas as pd
from help_function import calculate_metabolism, calculate_macros, get_diet, get_diet_products, get_physical_activity_id

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ilia123qweasdzxc@localhost:3306/healthy_people'

bcrypt = Bcrypt(app)
app.secret_key = bcrypt.generate_password_hash(
        '@!K@#@#DJSFHJSDjdshnjf@#t)2@4*%#djsf4^rew%^#@$D&*FDSdyf*&^#$%CBK').decode('utf-8')
db.init_app(app)
with app.app_context():
    db.create_all()
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', name=current_user.User_name, surname=current_user.User_surname)
    else:
        return render_template('index.html')


@app.route('/sign.html', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        data = request.form.to_dict()
        password_hash = bcrypt.generate_password_hash(data['Password_hash']).decode('utf-8')
        new_user = Users(User_name=data['User_name'], User_surname=data['User_surname'], Email=data['Email'],
                         Password_hash=password_hash)
        db.session.add(new_user)
        db.session.flush()
        db.session.commit()
        login_user(new_user)

        return jsonify(
                {'message'  : 'User registered and logged in!', 'user_id': new_user.User_id,
                 'user_name': new_user.User_name, 'user_surname': new_user.User_surname}), 201

    else:
        return render_template('/sign.html')


@app.route('/delete-account', methods=['POST'])
def delete_account():
    user_id = current_user.get_id()
    user = Users.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    logout()
    return render_template('index.html')


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        email = data['Email']
        password = data['Password']
        user = Users.query.filter_by(Email=email).first()
        if user and bcrypt.check_password_hash(user.Password_hash, password):
            login_user(user)
            return jsonify(
                    {'message'     : 'User logged in!', 'user_id': user.User_id, 'user_name': user.User_name,
                     'user_surname': user.User_surname}), 201
        else:
            return render_template('login.html', error='Неправильный логин или пароль')

    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/Home/<user_id>/<user_name>')
@login_required
def index_user(user_id, user_name):
    return render_template('Home.html', user_id=user_id,
                           name=user_name)


@app.route('/Home/<user_id>/diets', methods=['GET', 'POST'])
@login_required
def diets(user_id):
    if request.method == 'POST':
        if current_user.Diet_id is None:
            new_diet = Diets(Diet_name=str("Пользователь " + str(current_user.User_id)), Diet_calories=0,
                             Diet_proteins=0,
                             Diet_fats=0, Diet_carbohydrates=0)
            db.session.add(new_diet)
            db.session.commit()
            current_user.Diet_id = new_diet.Diet_id
            db.session.commit()
        data = request.form.to_dict()
        current_user.Weight = data['weight']
        current_user.Height = data['height']
        current_user.Age = data['age']
        if data['gender'] == 'female':
            current_user.Gender = 'F'
            current_user.Metabolism = calculate_metabolism(current_user.Weight, current_user.Height, current_user.Age,
                                                           data['Physical_activity'])
        else:
            current_user.Gender = 'M'
            current_user.Metabolism = calculate_metabolism(current_user.Weight, current_user.Height, current_user.Age,
                                                           data['Physical_activity'], data)

        current_user.Physical_activity_id = get_physical_activity_id(data['Physical_activity'])
        db.session.commit()
        proteins, fats, carbs = calculate_macros(current_user.Metabolism)
        db.session.commit()
        return render_template('diets.html', user_id=user_id, metabolism=current_user.Metabolism,
                               height=current_user.Height, weight=current_user.Weight, age=current_user.Age,
                               proteins=proteins, fats=fats, carbs=carbs)
    elif current_user.Diet_id is not None:
        diet = Diets.query.get(current_user.Diet_id)
        products = get_diet_products(diet.Diet_id)

        proteins, fats, carbs = calculate_macros(current_user.Metabolism)
        return render_template('diets.html', user_id=user_id,
                               metabolism=current_user.Metabolism,
                               height=current_user.Height, weight=current_user.Weight, age=current_user.Age,
                               proteins=proteins, fats=fats, carbs=carbs, products=products,
                               diet_calories=diet.Diet_calories,
                               diet_proteins=diet.Diet_proteins, diet_fats=diet.Diet_fats,
                               diet_carbs=diet.Diet_carbohydrates)
    else:
        return render_template('diets.html', user_id=user_id, diet=None)


@app.route('/delete_product', methods=['POST'])
@login_required
def delete_product():
    product_id = request.form.get('productId')
    product = ProductsDiets.query.filter_by(Product_id=product_id, Diet_id=current_user.Diet_id).first()

    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify(message="Продукт успешно удален из диеты.")
    else:
        return jsonify(error="Продукт не найден в диете."), 404


@app.route('/edit_weight', methods=['POST'])
@login_required
def edit_weight():
    product_id = request.form.get('productId')
    weight = request.form.get('weight')
    product = ProductsDiets.query.filter_by(Product_id=product_id, Diet_id=current_user.Diet_id).first()

    if product:
        product.Product_weight = weight
        db.session.commit()
        return jsonify(message="Вес продукта успешно изменен.")
    else:
        return jsonify(error="Продукт не найден в диете."), 404


@app.route('/search', methods=['POST'])
def search_products():
    data = request.form.to_dict()
    products = Products.query.filter(Products.Product_name.like('%' + data['search'] + '%')).all()
    serialized_products = []
    for product in products:
        serialized_product = {
                'Product_id'           : product.Product_id,
                'Product_name'         : product.Product_name,
                'Product_calories'     : product.Product_calories,
                'Product_proteins'     : product.Product_proteins,
                'Product_fats'         : product.Product_fats,
                'Product_carbohydrates': product.Product_carbohydrates
        }
        serialized_products.append(serialized_product)
    return jsonify({'products': serialized_products})


@app.route('/add_product', methods=['POST'])
def add_product_to_diet():
    data = request.form.to_dict()
    productId = data['productId']
    weight = data['weight']
    if current_user.Diet_id is None:
        new_diet = Diets(Diet_name=str("Пользователь " + current_user.User_id), Diet_calories=0, Diet_proteins=0,
                         Diet_fats=0, Diet_carbohydrates=0)
        db.session.add(new_diet)
        db.session.commit()
        current_user.Diet_id = new_diet.Diet_id
        db.session.commit()
    product = Products.query.get(productId)
    product_diet = ProductsDiets(Product_id=productId, Diet_id=current_user.Diet_id, Product_weight=weight)
    db.session.add(product_diet)
    db.session.commit()
    return jsonify({'message': 'Product added to diet'})


@app.route('/Home/<user_id>/training', methods=['GET', 'POST'])
@login_required
def training(user_id):
    if request.method == 'POST':
        data = request.form.to_dict()
        values_training = []
        if data['location'] == 'home':
            values_training.append(1)
        else:
            values_training.append(2)
        if data['frequency'] == 'two_days':
            values_training.append(1)
        else:
            values_training.append(2)
        if data['method'] == 'full_body':
            values_training.append(2)
        else:
            values_training.append(1)

        program = Programs.query.filter_by(Method_id=values_training[2], Place_id=values_training[0],
                                           Day_id=values_training[1]).order_by(func.random()).first()
        current_user.Program_id = program.Program_id
        exercises = Exercises.query.join(Exercises_programs).filter(
                Exercises_programs.Program_id == program.Program_id).all()

        db.session.commit()
        return render_template('training.html', user_id=user_id, exercises=exercises)
    elif current_user.Program_id is not None:
        program = Programs.query.filter_by(Program_id=current_user.Program_id).order_by(func.random()).first()
        exercises = Exercises.query.join(Exercises_programs).filter(
                Exercises_programs.Program_id == program.Program_id).all()
        return render_template('training.html', user_id=user_id, exercises=exercises)
    else:
        return render_template('training.html', user_id=user_id)


@app.route('/download/exercises', methods=['GET'])
def download_exercises():
    exercises = Exercises.query.join(Exercises_programs).filter(
            Exercises_programs.Program_id == current_user.Program_id).all()

    output = io.BytesIO()

    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    header_row = ['Тренировка', 'Упражнение', 'Количество подходов', 'Количество повторений']
    for col_num, col_val in enumerate(header_row):
        worksheet.write(0, col_num, col_val)

    training_number = 0
    for index, exercise in enumerate(exercises):
        if index % 5 == 0:
            training_number += 1
        row = [training_number, exercise.Exercise_name, exercise.Number_of_approaches,
               exercise.Number_of_repetitions]
        for col_num, col_val in enumerate(row):
            worksheet.write(index + 1, col_num, col_val)

    workbook.close()
    output.seek(0)
    xlsx_content = output.getvalue()

    response = Response(
            xlsx_content,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={'Content-Disposition': 'attachment;filename=program.xlsx'}
    )
    return response


@app.route('/Home/<user_id>/diets/download', endpoint='download_products', methods=['GET', 'POST'])
@login_required
def download_products(user_id):
    products = Products.query.join(ProductsDiets).filter(
            ProductsDiets.Diet_id == current_user.Diet_id).all()

    output = io.BytesIO()

    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    header_row = ['Продукт', 'Белки (г)', 'Жиры (г)', 'Углеводы (г)']
    for col_num, col_val in enumerate(header_row):
        worksheet.write(0, col_num, col_val)

    for index, product in enumerate(products):
        row = [product.Product_name, product.Product_proteins, product.Product_fats, product.Product_carbohydrates]
        for col_num, col_val in enumerate(row):
            worksheet.write(index + 1, col_num, col_val)

    workbook.close()
    output.seek(0)
    xlsx_content = output.getvalue()

    response = Response(
            xlsx_content,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={
                    'Content-Disposition': 'attachment; filename=products.xlsx'
            }
    )

    return response


@app.route('/Home/<user_id>/profile', methods=['GET', 'POST'])
@login_required
def profile(user_id):
    age = ""
    height = ""
    weight = ""
    metabolism = ""
    gender = ""
    if current_user.Age is not None:
        age = current_user.Age
    if current_user.Height is not None:
        height = current_user.Height
    if current_user.Weight is not None:
        weight = current_user.Weight
    if current_user.Metabolism is not None:
        metabolism = current_user.Metabolism

    if current_user.Gender == "F":
        gender = "Женский"
    else:
        gender = "Мужской"
    Physical_activity = ""
    if current_user.Physical_activity_id == 1:
        Physical_activity = "Базовый обмен веществ"
    elif current_user.Physical_activity_id == 2:
        Physical_activity = "Низкая активност"
    elif current_user.Physical_activity_id == 3:
        Physical_activity = "1-3 Тренировки в неделю"
    elif current_user.Physical_activity_id == 4:
        Physical_activity = "5 Тренировок в неделю"
    elif current_user.Physical_activity_id == 5:
        Physical_activity = "Ежедневные тренировки"
    _exercises = []
    _products = []
    if current_user.Diet_id is not None:
        _products = Products.query.join(ProductsDiets).filter(
                ProductsDiets.Diet_id == current_user.Diet_id).all()
    if current_user.Program_id is not None:
        _exercises = Exercises.query.join(Exercises_programs).filter(
                Exercises_programs.Program_id == current_user.Program_id).all()

    return render_template(
            'profile.html',
            name=current_user.User_name,
            surname=current_user.User_surname,
            age=age,
            height=height,
            weight=weight,
            metabolism=metabolism, gender=gender, Physical_activity=Physical_activity, products=_products,
            exercises=_exercises)


@app.route('/Home/download', methods=['GET'])
@login_required
def download_profile():
    data = {
            "Имя"                          : [current_user.User_name],
            "Фамилия"                      : [current_user.User_surname],
            "Возраст"                      : [current_user.Age] if current_user.Age is not None else [""],
            "Рост"                         : [current_user.Height] if current_user.Height is not None else [""],
            "Вес"                          : [current_user.Weight] if current_user.Weight is not None else [""],
            "Обмен веществ"                : [current_user.Metabolism] if current_user.Metabolism is not None else [""],
            "Пол"                          : ["Женский" if current_user.Gender == "F" else "Мужской"],
            "Уровень физической активности": [
                    "Базовый обмен веществ" if current_user.Physical_activity_id == 1 else
                    "Низкая активность" if current_user.Physical_activity_id == 2 else
                    "1-3 тренировки в неделю" if current_user.Physical_activity_id == 3 else
                    "5 тренировок в неделю" if current_user.Physical_activity_id == 4 else
                    "Ежедневные тренировки"
            ],
    }

    diet_data = {}
    if current_user.Diet_id is not None:
        diet_products = Products.query.join(ProductsDiets).filter(
                ProductsDiets.Diet_id == current_user.Diet_id).all()
        for i, p in enumerate(diet_products):
            diet_data[f"Название {i + 1}"] = [p.Product_name]
            diet_data[f"Калории {i + 1}"] = [p.Product_calories]
            diet_data[f"Белки {i + 1}"] = [p.Product_proteins]
            diet_data[f"Жиры {i + 1}"] = [p.Product_fats]
            diet_data[f"Углеводы {i + 1}"] = [p.Product_carbohydrates]

    workout_data = {}
    if current_user.Program_id is not None:
        program_exercises = Exercises.query.join(Exercises_programs).filter(
                Exercises_programs.Program_id == current_user.Program_id).all()
        for i, e in enumerate(program_exercises):
            workout_data[f"Название {i + 1}"] = [e.Exercise_name]
            workout_data[f"Количество подходов {i + 1}"] = [e.Number_of_approaches]
            workout_data[f"Количество повторений {i + 1}"] = [e.Number_of_repetitions]

    filename = f"{current_user.User_name}_{current_user.User_surname}_profile.xlsx"
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        df = pd.DataFrame.from_dict(data, orient="index")
        df.to_excel(writer, sheet_name='Профиль', header=False)

        if current_user.Diet_id is not None:
            df_diet = pd.DataFrame.from_dict(diet_data, orient="index")
        df_diet.to_excel(writer, sheet_name='Диета', header=False)
        if current_user.Program_id is not None:
            df_workout = pd.DataFrame.from_dict(workout_data, orient="index")
            df_workout.to_excel(writer, sheet_name='Тренировка', header=False)

    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
