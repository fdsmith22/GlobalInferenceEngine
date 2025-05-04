from flask import Flask
from app.routes.nodes import nodes_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(nodes_bp)
    return app
