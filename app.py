from flask import (
    Flask,
    render_template,
    # redirect,
    # url_for,
    # flash,
    # request,
    # make_response,
)
from database import Database

app = Flask(__name__, template_folder="./templates")
database = Database()


@app.teardown_appcontext
def teardown_app_context(exception):
    database.teardown_db()


@app.get("/")
def hello():
    db_connection = database.get_connection()
    return render_template("index.html")
