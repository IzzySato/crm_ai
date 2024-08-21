from flask import Blueprint, request, jsonify
from .services import generate_description
from .utils import require_auth
from flask_cors import CORS, cross_origin

main = Blueprint('main', __name__)

@main.route('/description', methods=['POST'])
@require_auth
def get_description():
    image_url = request.json['image_url']
    product_name = request.json['product_name']
    description = generate_description(image_url, product_name)
    return jsonify({ "description": description }), 200