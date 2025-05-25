from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    job = StringField('Описание работы', validators=[DataRequired()])
    team_leader = SelectField('Руководитель', coerce=int, validators=[DataRequired()])
    work_size = IntegerField('Часы', validators=[DataRequired()])
    collaborators = StringField('ID участников (через запятую)', validators=[DataRequired()])
    is_finished = BooleanField('Завершена ли?')

