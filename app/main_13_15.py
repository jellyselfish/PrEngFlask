from flask import Flask

from models import db
from models.users import User
from models.jobs import Job

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализируем модели
db.init_app(app)


def add_users():
    users = [
        User(surname='Иванов', name='Иван', age=30, position='Инженер', speciality='Механик',
             address='Москва', email='ivanov@example.com', hashed_password='pass1'),
        User(surname='Петров', name='Пётр', age=35, position='Главный инженер', speciality='Электроника',
             address='Санкт-Петербург', email='petrov@example.com', hashed_password='pass2'),
        User(surname='Сидоров', name='Александр', age=28, position='Техник', speciality='Автоматизация',
             address='Казань', email='sidorov@example.com', hashed_password='pass3')
    ]
    db.session.add_all(users)
    db.session.commit()
    print("Пользователи добавлены")


def add_jobs():
    jobs = [
        Job(team_leader=1, job='Разработка прототипа робота', work_size=120,
            collaborators='2,3', is_finished=True),
        Job(team_leader=2, job='Тестирование системы жизнеобеспечения', work_size=80,
            collaborators='1,3', is_finished=False),
        Job(team_leader=3, job='Настройка навигационной системы', work_size=60,
            collaborators='1', is_finished=True)
    ]
    db.session.add_all(jobs)
    db.session.commit()
    print("Работы добавлены")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  #

        if User.query.count() == 0:
            add_users()

        if Job.query.count() == 0:
            add_jobs()

