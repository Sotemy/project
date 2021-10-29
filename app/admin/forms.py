from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, TimeField, StringField, FileField, DecimalField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class AdvertisingForm(FlaskForm):
    title=StringField('title', validators=[DataRequired()])
    date=DateField('DatePicker', format='%Y-%m-%d')