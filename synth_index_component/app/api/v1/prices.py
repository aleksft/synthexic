from api_def import api

from flask import request
from flask.json import jsonify

from app.models.price import Price


# Save prices
@api.route('/prices', methods=['POST', 'PUT'])
def savePrices():
    response = False
    if request and request.get_json():
        response = Price(request.get_json()).save()
    return jsonify(response=response)
