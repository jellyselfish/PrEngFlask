from app.extensions import db


class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    chief = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    members = db.Column(db.String)  # Список id участников через запятую
    email = db.Column(db.String, unique=True)

    leader = db.relationship("User", foreign_keys=[chief])
