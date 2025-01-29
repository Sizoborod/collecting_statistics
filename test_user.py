from data.users import User
from flask import Flask
from data import db_session
from werkzeug.security import generate_password_hash


def set_password(password):
    return generate_password_hash(password)

db_session.global_init("db/base_statistics1.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
user = User()
user.name = 'Ridley'
user.email = 'scott_chief@mars.org'
user.hashed_password= set_password('123')
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()