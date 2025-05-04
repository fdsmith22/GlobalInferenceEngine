from flask import Flask
from redis import Redis
from .routes.nodes import nodes_bp
from config import Config

redis_client = None

def create_app():
    global redis_client
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Redis connection
    redis_client = Redis.from_url(app.config["REDIS_URL"], decode_responses=True)

    # Register routes
    app.register_blueprint(nodes_bp)

    return app
