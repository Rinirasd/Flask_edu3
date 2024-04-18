from config import app
from random import randint
from config import Flask, render_template

from models import Flat


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cats/")
def cats():
    cat_name = "Barsic"
    return render_template("cats.html", cat_name=cat_name)


@app.route("/info/<name>/<age>")
def info(name, age):
    text = f"<h2><i>Hi {name}, you are {age} y.o.</i></h2>"
    return text


@app.route("/random/<a>/<b>")
def random(a, b):
    r = randint(int(a), int(b))
    return str(r)


@app.route("/flats/")
def flats_view():
    flats = Flat.query.all()
    return render_template("flats.html", flats=flats)


app.run(host = "0.0.0.0", debug=True)
