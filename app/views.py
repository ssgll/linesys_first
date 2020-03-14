from app import index
from flask import render_template, url_for


def pageIndex():
    return render_template("index.html")