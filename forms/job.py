from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, \
    SubmitField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    team_leader = IntegerField('Leader id', validators=[DataRequired()])
    job = StringField('Описание работы', validators=[DataRequired()])
    work_size = IntegerField('Продолжительность (час)',
                             validators=[DataRequired()])
    collaborators = StringField('Список участников',
                                validators=[DataRequired()])
    is_finished = BooleanField('Работа завершена')
    submit = SubmitField('Добавить')
