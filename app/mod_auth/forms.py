# Import Form and RecaptchaField (optional)
from flask_wtf import Form # , RecaptchaField
# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField # BooleanField

# Import Form validators
from wtforms.validators import Required, Email, EqualTo, email_validator


# Define the login form (WTForms)

class LoginForm(Form):
    email    = TextField('Email Address', [Email(), Required(message='Forgot your email address?')])
    password = PasswordField('Password', [ Required(message='Must provide a password. ;-)')])

class RegisterForm(Form):
    email=TextField('Email Address', [Email(), Required(message='Forgot your email address?')])
    password = PasswordField('Password', [ Required(message='Must provide a password. ;-)')])
    password2 = PasswordField('Password again', [ Required(message='Must provide a password. ;-)')])