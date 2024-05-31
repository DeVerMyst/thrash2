from flask import Flask
from .models.user import db
from .routes.user_routes import user_bp
from flasgger import Swagger

# Configuration de Swagger UI avec la spécification YAML
swagger_config = {
    "openapi": "3.0.0",
    "title": "Mon API",
    "version": "1.0.0",
    "specs": [
        {
            "url": "/apidocs/openapi.yaml",
            "endpoint": "openapi",
            "route": "/apidocs/openapi.json"
        }
    ],
    "swagger_ui": True,
    "headers": [
        ("Content-Type", "application/json"),
        ("Access-Control-Allow-Origin", "*"),
    ],
}


def create_app():

    app = Flask(__name__)
    Swagger(app, config=swagger_config)

    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"

    db.init_app(app)

    app.register_blueprint(user_bp, url_prefix="/api")

    with app.app_context():
        db.create_all()
        print("Database created!")

    return app
