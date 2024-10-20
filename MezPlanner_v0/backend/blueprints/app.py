# -----------------
# File: File
# Description: App.py is the file that glue all the blueprints together
# Author: Menezess42
# Created: Sun 17:33 20/10/2024
# Last Modified: 17:33 20/10/2024
# -----------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    # each blueprint has his template folder
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./mezBase.db"

    db.init_app(app)

    # import and register all blueprints
    # from blueprints.core.routes import core
    # from blueprints.dayplanner.routes import dayplanner

    # app.register_blueprint(core, url_prefix="/")
    # app.register_blueprint(dayplanner, url_prefix="/dayplanner")

    migrate = Migrate(app, db)
    return app
