from flask import jsonify

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

api = Redprint('user')


@api.route('/<int:uid>')
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user)
