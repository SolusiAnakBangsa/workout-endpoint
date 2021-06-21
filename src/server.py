from flask import Flask
from flask.blueprints import Blueprint
import time
import config as c
import routes
import models

app = Flask(__name__)

# Set debug mode
app.debug = c.DEBUG

@app.route("/servertime")
def server_time():
    resp = {
        "unixtime": time.time(),
        "localtime": time.localtime()
    }
    return resp

# Registers all the routes
for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        # Register with url prefix and blueprint prefix
        app.register_blueprint(blueprint, url_prefix=(c.APP_ROOT + blueprint.url_prefix if blueprint.url_prefix else ""))

if __name__ == "__main__":
    app.run(port=c.PORT)