from flask import Blueprint, render_template, request
from services.api_client import get_api_response

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html", card=None, prev_id=None, next_id=None)

@main.route("/lookup", methods=["POST"])
def lookup():
    card_id = request.form["card_id"]
    pick = request.form.get("pick_index")

    results = get_api_response(card_id)

    if len(results) == 0:
        return render_template("index.html", card=None, error="Card not found")
    
    if pick is not None:
        card = results[int(pick)]
        return render_template("index.html", card=card, prev_id=None, next_id=None)

    if len(results) >= 2:
        return render_template("index.html", card=None, choices=results)
        
    return render_template("index.html", card=results[0], prev_id=None, next_id=None)