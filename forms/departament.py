from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class AddDepartamentForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    chief = IntegerField('Id руководителя', validators=[DataRequired()])
    members = StringField('Список участников', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Добавить')
