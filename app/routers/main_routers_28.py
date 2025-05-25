from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.extensions import db
from app.models.login_model import LoginUser
from app.models.users import User
from app.models.job_form import JobForm
from app.models.jobs import Job
from app.models.login_form import LoginForm
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('main', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.hashed_password == password:
            login_user(LoginUser(user))
            return redirect(url_for('main.show_jobs'))
        flash("Неверный логин или пароль", "danger")
    return render_template('login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        surname = request.form.get('surname')
        name = request.form.get('name')
        age = int(request.form.get('age'))
        position = request.form.get('position')
        speciality = request.form.get('speciality')
        address = request.form.get('address')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm_password')

        if password != confirm:
            flash("Пароли не совпадают", "danger")
            return redirect(url_for('main.register'))

        if User.query.filter_by(email=email).first():
            flash("Email занят", "danger")
            return redirect(url_for('main.register'))

        new_user = User(
            surname=surname,
            name=name,
            age=age,
            position=position,
            speciality=speciality,
            address=address,
            email=email
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html')


@bp.route('/add-job', methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobForm()
    form.team_leader.choices = [(u.id, u.name) for u in User.query.all()]
    if form.validate_on_submit():
        job = Job(
            job=form.job.data,
            team_leader=form.team_leader.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data
        )
        db.session.add(job)
        db.session.commit()
        return redirect(url_for('main.show_jobs'))
    return render_template('add_job.html', form=form)


@bp.route('/')
@bp.route('/jobs')
@login_required
def show_jobs():
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@bp.route('/edit-job/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    job = Job.query.get_or_404(id)
    if current_user.id != job.team_leader and current_user.id != 1:
        flash("Нет прав для редактирования", "danger")
        return redirect(url_for('main.show_jobs'))

    form = JobForm(obj=job)
    form.team_leader.choices = [(u.id, u.name) for u in User.query.all()]

    if form.validate_on_submit():
        form.populate_obj(job)
        db.session.commit()
        return redirect(url_for('main.show_jobs'))

    return render_template('add_job.html', form=form)


@bp.route('/delete-job/<int:id>')
@login_required
def delete_job(id):
    job = Job.query.get_or_404(id)
    if current_user.id != job.team_leader and current_user.id != 1:
        flash("Нет прав для удаления", "danger")
        return redirect(url_for('main.show_jobs'))

    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('main.show_jobs'))
