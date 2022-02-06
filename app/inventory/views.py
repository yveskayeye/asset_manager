from flask import Blueprint, render_template

inventory_bp = Blueprint("inventory_bp", __name__, template_folder="templates",
                        static_folder="static")

@inventory_bp.route("/")
def inventory():
    return render_template("inventory/inventory")