from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .views import views


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secretkey"
    app.register_blueprint(views, url_prefix="/")
    return app
