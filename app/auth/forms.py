from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email=StringField('Enter your email address', validators=[Required(), Email()])
    username=StringField('Enter your username', validators=[Required()])
    password=PasswordField('Input password', validators=[Required(), EqualTo('confirm_password', message='Passwords do not match')])
    confirm_password=PasswordField('Confirm Password', validators=[Required()])
    submit=SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('An account with that email exists')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('An account with that username exists')

class LoginForm(FlaskForm):
    email=StringField('Enter Your Email Address', validators=[Required(), Email()])
    password=PasswordField('Input your password', validators=[Required()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')