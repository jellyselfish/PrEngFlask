from app.models.users import User
from flask_login import UserMixin


class LoginUser(UserMixin):
    def __init__(self, user):
        self.id = user.id
        self.name = user.name
        self.email = user.email
        self.hashed_password = user.hashed_password

    def get_id(self):
        return str(self.id)

    @staticmethod
    def get(user_id):
        from app.models.users import User
        user = User.query.get(int(user_id))
        if user:
            return LoginUser(user)
        return None

