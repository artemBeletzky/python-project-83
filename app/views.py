from flask import (
    render_template,
    # redirect,
    # url_for,
    # flash,
    # request,
    # make_response,
)

from postgres import Postgres
from .app import create_app

app = create_app()
db = Postgres()


@app.teardown_appcontext
def close_db_connection(exception):
    db.close_conn(exception=exception)


@app.get("/")
def hello():
    db.connect()
    db.execute_modifying_query(
        query="INSERT INTO urls (name, created_at) VALUES ('example.cock', NOW())"
    )
    db.execute_modifying_query(
        query="INSERT INTO urls (name, created_at) VALUES ('another_example.cock', NOW())"
    )
    print(db.fetch_data("SELECT * FROM urls", fetchall=True))
    return render_template("index.html")
