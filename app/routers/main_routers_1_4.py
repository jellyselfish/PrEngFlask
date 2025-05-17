from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def home():
    return render_template('home.html')


@main_bp.route('/index')
def index():
    return render_template('index.html')


@main_bp.route('/promotion')
def promotion():
    return render_template('promotion.html')


@main_bp.route('/image')
def image():
    return render_template('image.html')


@main_bp.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')

