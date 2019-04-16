import os

from flask import Flask, jsonify
from config import ProdConfig, DevConfig
from extensions import db


def create_app():
    """An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/
    """
    if os.getenv("FLASK_ENV") == 'prod':
        config_object = ProdConfig
    else:
        config_object = DevConfig
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_middleware(app)

    return app


def register_extensions(app):
    db.init_app(app)
    # migrate.init_app(app, db)


def register_middleware(app):
    @app.before_request
    def before_request():
        pass

    @app.after_request
    def after_request(data):
        return data


def register_blueprints(app):
    from .docs import bp as doc_bp
    app.register_blueprint(doc_bp)
    from .feedback import bp as fb_bp
    app.register_blueprint(fb_bp)
    from .files import bp as files_bp
    app.register_blueprint(files_bp)


def response(data=None, code=200, msg=''):
    if isinstance(data, list):
        if data and isinstance(data[0], db.Model):
            res = [item.to_json for item in data]
        else:
            res = data
        return jsonify(code=code, msg=msg, data={'list': res})
    elif isinstance(data, db.Model):
        return jsonify(code=code, msg=msg, data=data.to_json)
    else:
        return jsonify(code=code, msg=msg, data=data)
