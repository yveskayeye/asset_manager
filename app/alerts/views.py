from crypt import methods
from flask import Blueprint ,render_template
from flask_login import login_required

alert_bp = Blueprint("alert_bp", __name__, template_folder="templates",
                    static_folder="static")


@alert_bp.route("/", methods=["GET", "POST"])
def track():
    return render_template("alerts/alerts.html")