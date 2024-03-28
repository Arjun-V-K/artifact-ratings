""" Application factory """

import os
from flask import Flask

from app.db import db
from app.routes import artifact


def create_app():
    """ Create app, register blueprints and DB """
    app = Flask(__name__, instance_relative_config=True)

    # Set default config
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///site.sqlite',
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    # Set config from instance config, if it exists
    app.config.from_pyfile('config.py', silent=True)

    # Register database
    db.init_app(app)

    # Register modules
    app.register_blueprint(artifact.bp)

    app.add_url_rule('/', endpoint='artifact.welcome')

    return app
