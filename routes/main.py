from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route('/')
def index():
    return render_template("index.html", card=None, prev_id=None, next_id=None)

@main.route("/lookup")
def lookup():
    return "meh"