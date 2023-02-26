from flask import Flask, request, jsonify, render_template, redirect, url_for, session, make_response, Response
from flask_login import LoginManager, login_user, login_required, UserMixin, current_user
from flask_bcrypt import Bcrypt
from my_classes import db, Users, Physical_activity, Methods, Days, Places, Programs, Exercises, Exercises_programs
from sqlalchemy import func

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


@app.route('/Home/<user_id>/<user_name>/<user_surname>')
@login_required
def index_user(user_id, user_name, user_surname):
    return render_template('Home.html', user_id=user_id,
                           name=user_name, surname=user_surname)


@app.route('/Home/<user_id>/<username>/diets', methods=['GET', 'POST'])
@login_required
def diets(user_id, username):
    if request.method == 'POST':
        data = request.form.to_dict()
        current_user.Weight = data['weight']
        current_user.Height = data['height']
        current_user.Age = data['age']
        if data['gender'] == 'female':
            current_user.Gender = 'F'
            current_user.Metabolism = int((655 + (9.6 * int(current_user.Weight)) + (1.8 * int(current_user.Height)) - (
                    4.7 * int(current_user.Age))) * float(data['Physical_activity']))
        else:
            current_user.Gender = "M"
            current_user.Metabolism = int((66 + (13.7 * int(current_user.Weight)) + (5 * int(current_user.Height)) - (
                    6.8 * int(current_user.Age))) * float(data['Physical_activity']))

        if data['Physical_activity'] == '1':
            current_user.Physical_activity_id = 1
        elif data['Physical_activity'] == '1.2':
            current_user.Physical_activity_id = 2
        elif data['Physical_activity'] == '1.375':
            current_user.Physical_activity_id = 3
        elif data['Physical_activity'] == '1.55':
            current_user.Physical_activity_id = 4
        elif data['Physical_activity'] == '1.6375':
            current_user.Physical_activity_id = 5

        db.session.commit()
        proteins = int((current_user.Metabolism * 0.45) // 4)
        fats = int((current_user.Metabolism * 0.2) // 9)
        carbs = int((current_user.Metabolism * 0.35) // 4)
        return render_template('diets.html', user_id=user_id, username=username, metabolism=current_user.Metabolism,
                               height=current_user.Height, weight=current_user.Weight, age=current_user.Age,
                               proteins=proteins, fats=fats, carbs=carbs)

    elif current_user.Weight is not None:
        return render_template('diets.html', user_id=user_id, username=username,
                               metabolism=current_user.Metabolism,
                               height=current_user.Height, weight=current_user.Weight, age=current_user.Age,
                               proteins=int((current_user.Metabolism * 0.45) // 4),
                               fats=int((current_user.Metabolism * 0.2) // 9),
                               carbs=int((current_user.Metabolism * 0.35) // 4))
    else:
        return render_template('diets.html', user_id=user_id, username=username)


@app.route('/Home/<user_id>/<username>/training', methods=['GET', 'POST'])
@login_required
def training(user_id, username):
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
        return render_template('training.html', user_id=user_id, username=username, exercises=exercises)
    elif current_user.Program_id is not None:
        program = Programs.query.filter_by(Program_id=current_user.Program_id).order_by(func.random()).first()
        exercises = Exercises.query.join(Exercises_programs).filter(
                Exercises_programs.Program_id == program.Program_id).all()
        return render_template('training.html', user_id=user_id, username=username, exercises=exercises)
    else:
        return render_template('training.html', user_id=user_id, username=username)


import io
import xlsxwriter


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
        if index % 6 == 0:
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


if __name__ == '__main__':
    app.run(debug=True)
