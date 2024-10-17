from flask import render_template, Blueprint

dayplanner = Blueprint(
    "dayplanner", __name__, template_folder="templates", static_folder="static"
)


@dayplanner.route("/")
def index():
    return render_template("dayplanner/index.html")
