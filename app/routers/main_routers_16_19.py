from flask import Blueprint, render_template, request, redirect, url_for
from app.extensions import db
from app.models.jobs import Job
from app.models.users import User

bp = Blueprint('main_16_19', __name__)


@bp.route('/jobs')
def show_jobs():
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        password = request.form.get('password')
        confirm = request.form.get('confirm_password')
        if password != confirm:
            return "Пароли не совпадают"

        user = User(
            surname=request.form.get('surname'),
            name=request.form.get('name'),
            age=int(request.form.get('age')),
            position=request.form.get('position'),
            speciality=request.form.get('speciality'),
            address=request.form.get('address'),
            email=request.form.get('email'),
            hashed_password=password
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.show_jobs'))
    return render_template('register.html')

