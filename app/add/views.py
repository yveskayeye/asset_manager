from re import A
from flask import Blueprint, flash,render_template
from flask_login import login_required
from ..models import Asset, db
from .forms import AddForm

add_bp = Blueprint("add_bp", __name__, template_folder="templates",
                    static_folder="static")


@add_bp.route("/", methods=["POST", "GET"])
@login_required
def add():
    add_form = AddForm()
    
    if add_form.validate_on_submit():
        asset = Asset(asset_tag=get_tag(), name=add_form.name.data, type=add_form.type.data,
                        item_discription=add_form.item_discription.data, condition=add_form.condition.data,
                        serial=add_form.serial.data, date_manufactured=add_form.date_manufactured.data,
                        cost=add_form.cost.data, purchase_date=add_form.purchase_date.data)
        
        db.session.add(asset)
        db.session.commit()

        flash("Asset added succesfully", category="success")
        
    return render_template("add/add.html", form=add_form)


def get_tag():
    import string
    import random

    all_chars = string.ascii_letters + string.digits
    # print(all_chars)

    chars_count = len(all_chars)
    # print(chars_count)

    serial_list = " "
    count = 10

    while count > 0:

        random_number = random.randint(0, chars_count - 1)

        random_character = all_chars[random_number]

        serial_list += random_character

        count -= 1  # count = count - 1

    return serial_list
