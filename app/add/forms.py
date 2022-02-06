from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AddForm(FlaskForm):
    type = StringField(label="Type", validators=[])