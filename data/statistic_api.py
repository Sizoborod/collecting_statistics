from flask import jsonify, Blueprint, request, make_response
from werkzeug.security import generate_password_hash

from data import db_session
from data.users import User

blueprint = Blueprint('statistics_api', __name__, template_folder='templates')




@blueprint.route('/api/statistic')
def get_statistic():
    return ' re'


