from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route("/login")
def home():
    return "Login"


@auth.route("/sign-up")
def sign_up():
    return "Sign up"


@auth.route("/logout")
def logout():
    return "Logout"
