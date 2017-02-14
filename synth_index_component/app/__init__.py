import os

from flask import Flask

from app.settings import ProdConfig, DevConfig
from app.api.v1.api_def import api


if os.getenv("FLASK_ENV") == 'prod':
    DefaultConfig = ProdConfig
else:
    DefaultConfig = DevConfig


def create_app(config_object=DefaultConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(api)
    return app
