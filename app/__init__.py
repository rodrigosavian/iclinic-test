import os

from flask import Flask

from app import db


def create_app(config=None):
    # create flask app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        PROJECT_PATH=os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..')
        )
    )

    if config:
        app.config.update(config)

    # init all datasets
    db.init(app)

    # health check
    @app.route('/health')
    def health():
        return ''

    from app.patients.controller import bp as patients_bp

    # register patients
    app.register_blueprint(patients_bp)

    return app
