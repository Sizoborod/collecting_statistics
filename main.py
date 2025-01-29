import sys

import requests
from flask import Flask, render_template, redirect, make_response, jsonify, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import abort
from requests import get

from data import db_session, statistic_api, users_api


from data.users import User
from data.statistics import Statistic


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api_key = "40d1649f-0493-4b70-98ba-98533de7710b"
db_session.global_init("db/base_statistics.db")





@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': f'Not found ({error})'}), 404)



@app.route("/")
@app.route("/index")
def index():

    return "OK"



'''@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Register', form=form,
                                   message="Passwords don't match")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Register', form=form,
                                   message="This user already exists")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            email=form.email.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)'''






def main():
    db_session.global_init("db/base_statistics.db")
    # app.register_blueprint(statistic_api.blueprint)
    app.register_blueprint(users_api.blueprint)

    app.run()


if __name__ == '__main__':
    main()
