from flask import Blueprint, render_template, request, redirect, url_for
import os

bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('base.html', title="Главная")


@bp.route('/form')
def form():
    return render_template('form2.html')


@bp.route('/<title>')
def custom_title(title):
    return render_template('base.html', title=title)


@bp.route('/list_prof/<list_type>')
def list_prof(list_type):
    professions = [
        "Инженер по жизниобеспечению",
        "Медик",
        "Пилот",
        "Программист",
        "Геолог",
        "Биолог"
    ]
    return render_template('list_prof.html', list_type=list_type, professions=professions)


@bp.route('/answer')
@bp.route('/auto_answer', methods=['GET', 'POST'])
def answer():
    if request.method == 'POST':
        data = {
            'fullname': request.form.get('fullname'),
            'birthdate': request.form.get('birthdate'),
            'gender': request.form.get('gender'),
            'education': request.form.get('education'),
            'job': request.form.get('job'),
            'address': request.form.get('address'),
            'phone': request.form.get('phone'),
            'email': request.form.get('email')
        }
        return render_template('auto_answer.html', **data)
    return redirect(url_for('main.form'))



