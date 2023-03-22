from app import app
from flask import render_template


@app.route("/")
def main():
    return render_template("main/index.html")


@app.route("/calc/<int:x>/<int:y>")
def calc(x, y):
    return render_template("main/calc.html", x=x, y=y, sum=x+y)