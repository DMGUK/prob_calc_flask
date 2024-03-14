from flask import Flask
import config

def create_app(config_name='development'):
    app = Flask(__name__)

    from config import DevelopmentConfig, ProductionConfig

    if config_name == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    with app.app_context():
        from .homepage.views import homepage
        from .calc.views import calc

        app.register_blueprint(homepage)
        app.register_blueprint(calc)

    return app
