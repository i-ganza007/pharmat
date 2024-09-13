from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , EmailField
from wtforms.validators import DataRequired , Length , Email , EqualTo


class RegistrationForm(FlaskForm):
    firstname = StringField('Enter your first name',validators=[DataRequired(),Length(max=20)])
    lastname = StringField('Enter your last name',validators=[DataRequired(),Length(max=20)])
    email = EmailField('Enter your email',validators=[DataRequired(),Email()])
    password = PasswordField('Enter your password',validators=[DataRequired(),Length(max=8)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = EmailField('Enter your email',validators=[DataRequired(),Email()])
    password = PasswordField('Enter your password',validators=[DataRequired(),Length(max=8)])
    submit = SubmitField('Submit')



