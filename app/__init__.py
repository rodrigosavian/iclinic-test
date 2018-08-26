import os

from flask import Flask


def create_app(config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        PROJECT_PATH=os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..')
        )
    )

    if config:
        app.config.update(config)

    @app.route('/health')
    def health():
        return ''

    # # apply the blueprints to the app
    from app.patients.controller import bp as patients_bp
    app.register_blueprint(patients_bp)

    return app
