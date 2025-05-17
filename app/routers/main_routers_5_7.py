from flask import Blueprint, render_template, request, redirect, url_for
import os
main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/form')
def form():
    return render_template('form.html')


@main_bp.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return render_template('results.html', nickname=nickname, level=level, rating=rating)


@main_bp.route('/submit', methods=['POST'])
def submit():
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
    return "Данные успешно отправлены! <a href='/'>На главную</a>"


@main_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    photo_url = None
    if request.method == 'POST':
        file = request.files.get('photo')
        if file and file.filename != '':
            filename = file.filename
            file.save(os.path.join("static/uploads", filename))
            photo_url = url_for('static', filename=f'uploads/{filename}')
    return render_template('upload.html', photo_url=photo_url)
