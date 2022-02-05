from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[])
    password = PasswordField(label="Password")
    submit = SubmitField(label="login")

class SignupForm(FlaskForm):
    new_email = StringField(label="New Email")
    new_password = StringField(label="Create password")
    submit = SubmitField(label="Create account")