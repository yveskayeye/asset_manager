from multiprocessing import Condition
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    type = StringField(label="Type", validators=[DataRequired()])
    item_discription = StringField(label="Discription", validators=[DataRequired()])
    condition = StringField(label="Condition", validators=[DataRequired()])
    serial = StringField(label="Serial Number", validators=[DataRequired()])
    date_manufactured = StringField(label="Date Manufactured", validators=[DataRequired()])
    cost = StringField(label="Cost", validators=[DataRequired()])
    purchase_date = StringField(label="Purchase Date", validators=[DataRequired()])
    submit = SubmitField(label="Save")