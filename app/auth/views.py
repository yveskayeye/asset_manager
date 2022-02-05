from crypt import methods
from flask import Blueprint, render_template
from ..models import users
from .forms import LoginForm, SignupForm

auth_bp = Blueprint("auth_bp", __name__, template_folder="templates",
                    static_folder="static")



@auth_bp.route("/", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    return render_template("auth/login.html", form=login_form, form_type="Login")

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    signup_form = SignupForm()
    signup_form.validate_on_submit()
    return render_template("auth/login.html", form=signup_form, form_type="Signup")