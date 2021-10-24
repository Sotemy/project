# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm, RecaptchaField # , RecaptchaField
# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField, StringField # BooleanField

# Import Form validators
from wtforms.validators import Required, Email, EqualTo, DataRequired


# Define the login form (WTForms)

class LoginForm(FlaskForm):
    email    = TextField('Email Address', [Email(), Required(message='Forgot your email address?')])
    password = PasswordField('Password', [ Required(message='Must provide a password. ;-)')])
    recaptcha = RecaptchaField()

class RegisterForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email=TextField('Email Address', [Email(), Required(message='Forgot your email address?')])
    password = PasswordField('Password', [ Required(message='Must provide a password. ;-)')])
    password2 = PasswordField('Password again', [ Required(message='Must provide a password. ;-)'), EqualTo('password')])
    recaptcha = RecaptchaField()