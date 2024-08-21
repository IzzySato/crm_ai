import jwt
import os
from flask import jsonify

def verify_token(token):
  """
  Verifies a JWT token and returns the payload if valid
  """
  try:
    jwt.decode(token, os.getenv('JWT_SECRET_KEY'), algorithms=['HS256'])
  except jwt.ExpiredSignatureError:
    return jsonify({"message": "Token has expired"}), 401
  except jwt.InvalidTokenError:
    return jsonify({"message": "Invalid token"}), 401

