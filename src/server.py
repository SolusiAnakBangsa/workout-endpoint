from flask import Flask
from flask.blueprints import Blueprint
import config as c
import routes
import models

app = Flask(__name__)

# Set debug mode
app.debug = c.DEBUG

# Registers all the routes
for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        # Register with url prefix and blueprint prefix
        app.register_blueprint(blueprint, url_prefix=(c.APP_ROOT + blueprint.url_prefix if blueprint.url_prefix else ""))

if __name__ == "__main__":
    app.run(port=c.PORT)