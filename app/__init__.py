from flask import Flask
from .routes import main
from config import config
from flask_cors import CORS

def create_app(config_name='default'):
  app = Flask(__name__)
  CORS(app, supports_credentials=True, resources={
    r"/*": {
        "origins": "http://localhost:3000",
        "methods": ["GET", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"],
        "allow_headers": ["X-Requested-With", "Content-Type", "Authorization"],
        "supports_credentials": True
    }
  })
  app.config.from_object(config[config_name])
  app.register_blueprint(main)
  return app