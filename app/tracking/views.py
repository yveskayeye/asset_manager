from crypt import methods
from flask import Blueprint ,render_template
from flask_login import login_required

tracking_bp = Blueprint("tracking_bp", __name__, template_folder="templates",
                    static_folder="static")


@tracking_bp.route("/", methods=["GET", "POST"])
def track():
    return render_template("due-date-tracking/due-date-tracking.html")