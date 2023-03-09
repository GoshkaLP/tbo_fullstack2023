from flask import Flask

import config
from typing import Type
from app.views.locations import locations
from app.views.node import node


def create_app(app_config: Type[config.ProdConfig] | Type[config.DevConfig] | None = None) -> Flask | None:
    app = Flask(__name__, instance_relative_config=False)

    if app_config is None:
        return None

    app.config.from_object(app_config)

    app.register_blueprint(node)
    app.register_blueprint(locations)

    return app
