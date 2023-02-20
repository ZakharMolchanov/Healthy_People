from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ilia123qweasdzxc@localhost:3306/healthy_people'

bcrypt = Bcrypt(app)
app.secret_key = bcrypt.generate_password_hash(
        '@!K@#@#DJSFHJSDjdshnjf@#t)2@4*%#djsf4^rew%^#@$D&*FDSdyf*&^#$%CBK').decode('utf-8')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class Users(db.Model, UserMixin):
    User_id = db.Column(db.Integer, primary_key=True)
    User_name = db.Column(db.String(80), unique=False, nullable=False)
    User_surname = db.Column(db.String(80), unique=False, nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)
    Password_hash = db.Column(db.String(256), unique=False, nullable=False)

    def get_id(self):
        return self.User_id


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
        session = db.session()
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


@app.route('/Home/<user_name>/<user_surname>')
@login_required
def index_user(user_name, user_surname):
    return render_template('Home.html', name=user_name, surname=user_surname)


if __name__ == '__main__':
    app.run(debug=True)
