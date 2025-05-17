import json
import random
from flask import render_template, Blueprint

bp = Blueprint('main', __name__)


@bp.route('/member')
def member():
    with open('templates/crew.json', 'r', encoding='utf-8') as f:
        crew = json.load(f)
    selected_member = random.choice(crew)
    return render_template('member.html', member=selected_member)

