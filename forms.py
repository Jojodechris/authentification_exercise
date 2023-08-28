from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


 
class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    email=StringField("Email", validators=[InputRequired()])
    first_name=StringField("first name", validators=[InputRequired()])
    last_name=StringField("last name", validators=[InputRequired()])


    