# -----------------
# File: app.py
# Description: File responsible to run all the blueprints routes
# Author: Menezess42
# Notes: Blueprint is a way of using flask in a more modularized and
# professional way. Makes the code more powerfull and allows multiple

# devs to work in different modules without get in the way of one another
# -----------------
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    # each blueprint has his template folder
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./mezPlannerDB.db"

    db.init_app(app)

    # import and register all blueprints
    from blueprints.core.routes import core
    from blueprints.dayplanner.routes import dayplanner

    app.register_blueprint(core, url_prefix="/")
    app.register_blueprint(dayplanner, url_prefix="/dayplanner")

    migrate = Migrate(app, db)
    return app
