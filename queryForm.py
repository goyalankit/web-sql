__author__ = 'ankit'

from flask_wtf import Form, RecaptchaField
from wtforms import TextField, ValidationError, SubmitField, IntegerField, validators


class TelephoneForm(Form):
    country_code = IntegerField('Country Code', [validators.required()])
    area_code = IntegerField('Area Code/Exchange', [validators.required()])
    number = TextField('Number')

class QueryForm(Form):
    url = TextField('Webpage', description='Enter the URL of the web page you want to profile')
    # Uncomment to activate captcha
    #recaptcha = RecaptchaField('A sample recaptcha field')
    submit_button = SubmitField("Run")


    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')