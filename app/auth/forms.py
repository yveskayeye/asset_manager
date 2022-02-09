from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from ..models import User

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="login")




class SignupForm(FlaskForm):
    new_email = StringField(label="New Email", validators=[DataRequired(), Email()])
    new_password = StringField(label="Create password", validators=[DataRequired(), EqualTo("confirm_password")])
    confirm_password = PasswordField("Confirm Password")
    submit = SubmitField(label="Create account")

    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationErr("Email is already in use")