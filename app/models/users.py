from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    surname = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    position = db.Column(db.String)
    speciality = db.Column(db.String)
    address = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    modified_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.id} | {self.name} {self.surname}>'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'surname': self.surname,
            'name': self.name,
            'age': self.age,
            'position': self.position,
            'speciality': self.speciality,
            'address': self.address,
            'email': self.email,
            'modified_date': self.modified_date.isoformat() if self.modified_date else None
        }
