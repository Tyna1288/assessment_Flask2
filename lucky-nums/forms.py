from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Email


class UserForm(FlaskForm):
    name = StringField("name", validators=[InputRequired()])
    birthYear = StringField("year", validators=[InputRequired(message="must be between 1900 and 2000")])
    email = StringField("E-mail", validators=[InputRequired(), Email()])
    color = StringField("color", validators=[InputRequired(message="must be one of 'red', 'green', 'orange', 'blue'")])
   

