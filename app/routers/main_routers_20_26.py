from flask import Blueprint, render_template, request, redirect, url_for, session
from app.extensions import db
from app.models.login_model import LoginUser
from app.models.users import User
from app.models.job_form import JobForm
from app.models.jobs import Job
from flask_login import login_user, login_required, current_user

bp = Blueprint('main', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.hashed_password == password:
            login_user(LoginUser(user))
            return redirect(url_for('main_16_19.show_jobs'))

    return render_template('login.html')


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
        return redirect(url_for('main_16_19.show_jobs'))
    return render_template('add_job.html', form=form)

@bp.route('/edit-job/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    job = Job.query.get_or_404(id)
    if current_user.id != job.team_leader and current_user.id != 1:
        return "Нет прав", 403

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
        return "Нет прав", 403

    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('main_16_19.show_jobs'))
