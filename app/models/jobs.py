from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .users import User
from . import db


class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_leader = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job = db.Column(db.String, nullable=False)  # Описание работы
    work_size = db.Column(db.Integer, default=0)  # Объем работы в часах
    collaborators = db.Column(db.String)  # Список id участников как строка
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    is_finished = db.Column(db.Boolean, default=False)

    leader = db.relationship(lambda: User, foreign_keys=[team_leader])
