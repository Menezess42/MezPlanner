from flask import render_template, Blueprint

core = Blueprint("core", __name__,
                 template_folder="templates",
                 static_folder="static")


@core.route("/")
def index():
    return render_template("core/index.html")
