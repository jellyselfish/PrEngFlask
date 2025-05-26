from flask import Flask
from flask_login import LoginManager

from app.extensions import db
from routers.main_routers_28 import bp
from jobs_api import jobs_api
from user_api import users_api


from app.models.login_model import LoginUser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'main.login'


@login_manager.user_loader
def load_user(user_id):
    return LoginUser.get(user_id)


def global_init(db_name):
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}?check_same_thread=False'
    from models.users import User
    from models.jobs import Job
    from models.departments import Department


def create_session():
    return db.session


app.register_blueprint(bp)
app.register_blueprint(jobs_api)
app.register_blueprint(users_api)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, port=8080)

