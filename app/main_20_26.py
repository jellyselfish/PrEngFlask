from flask import Flask
from flask_login import LoginManager

from app.extensions import db
from routers.main_routers_20_26 import bp
from routers.main_routers_16_19 import bp as bp2

from app.models.users import User
from app.models.jobs import Job
from app.models.departments import Department

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


def query_department_users():
    session = create_session()

    # Выбираем пользователей из департамента id=1, у которых work_size > 25
    result = (
        session.query(User)
        .join(Job, User.id == Job.team_leader)
        .join(Department, Department.id == User.id)
        .filter(Department.id == 1)
        .filter(Job.work_size > 25)
        .all()
    )

    for user in result:
        print(f"{user.surname} {user.name}")


app.register_blueprint(bp)
app.register_blueprint(bp2)

with app.app_context():
    db.create_all()

    user = User.query.first()
    login_user = LoginUser.get(user.id)

    print(login_user.id)
    print(login_user.name)

if __name__ == '__main__':
    with app.app_context():
        # global_init("firm.db")
        query_department_users()
    app.run(debug=True, port=8080)
    print(id(db))
