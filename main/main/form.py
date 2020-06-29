from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, AnyOf


class PasscodeForm(FlaskForm):
    passcode = StringField('Passcode', validators=[DataRequired(),
                                                   AnyOf('Wir sind am leben', message='Nope.', values_formatter=None)])
    submit = SubmitField('Yes!')

