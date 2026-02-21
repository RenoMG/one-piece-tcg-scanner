import requests
from config import OP_API

def get_api_response(card_id):
    response = requests.get(f"{OP_API}/{card_id}/")
    response_text = response.json()

    return response_text