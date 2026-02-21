from flask import Blueprint, render_template
from services.api_client import get_api_response

main = Blueprint("main", __name__)

@main.route('/')
def index():
    return render_template("index.html", card=None, prev_id=None, next_id=None)

@main.route("/lookup")
def lookup():
    print(get_api_response("OP01-001"))
    return render_template("index.html", card=None, prev_id=None, next_id=None)