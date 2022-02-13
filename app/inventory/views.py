from flask import Blueprint, render_template
from ..models import Asset

inventory_bp = Blueprint("inventory_bp", __name__, template_folder="templates",
                        static_folder="static")

@inventory_bp.route("/")
def inventory():
    assets = Asset.query.all()
    return render_template("inventory/inventory.html", assets=assets)