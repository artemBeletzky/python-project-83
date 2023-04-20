from flask import (
    Flask,
    render_template,
)

# redirect,
# url_for,
# flash,
# request,
# make_response,

app = Flask(__name__, template_folder="../templates")


@app.get("/")
def hello():
    return render_template("index.html")
