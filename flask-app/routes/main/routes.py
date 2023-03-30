from app import app
from models import Article
from flask import render_template


@app.route("/")
def main():
    articles = Article.query.all()
    return render_template("main/index.html", articles=articles)


@app.route("/article/<int:id>")
def article_details(id):
    article = Article.query.get(id)
    return render_template("main/article_detail.html", article=article)


@app.route("/calc/<int:x>/<int:y>")
def calc(x, y):
    return render_template("main/calc.html", x=x, y=y, sum=x+y)