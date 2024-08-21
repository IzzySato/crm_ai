from functools import wraps
from flask import request, jsonify
from ..services.jwt_service import verify_token

def require_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    token = request.headers.get('Authorization')
    if not token:
      return jsonify({ "message": "Authorization header is missing"}), 401
    verify_token(token)
    return f(*args, **kwargs)
  return decorated