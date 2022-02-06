from flask import Blueprint,render_template
from flask_login import login_required
from ..models import db
from .forms import AddForm

add_bp = Blueprint("add_bp", __name__, template_folder="templates",
                    static_folder="static")


@add_bp.route("/", methods=["POST"])
@login_required
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        pass
    return render_template("add/add.html")