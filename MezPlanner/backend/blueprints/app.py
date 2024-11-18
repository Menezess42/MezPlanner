# -----------------
# File: File
# Description: App.py is the file that glue all the blueprints together
# Author: Menezess42
# Created: Sun 17:33 20/10/2024
# Last Modifiate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    # each blueprint has his template folder
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./mezBase.db"
    app.config["SECRET_KEY"] = "Temporary_secret_key_for_app_MezPlanner"
    db.init_app(app)
    bcrypt.init_app(app)
    # from blueprints.user.routes import user
    # from blueprints.task.routes import task
    # app.register_blueprint(user, url_prefix="/user")
    # app.register_blueprint(task, url_prefix="/task")

    migrate = Migrate(app, db)
    return app
