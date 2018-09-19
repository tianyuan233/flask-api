from flask import Blueprint

from ginger.app.libs.redprint import Redprint

# user = Blueprint('user', __name__)

api = Redprint('user')

@api.route('/get')
def get_book():
    return 'book'