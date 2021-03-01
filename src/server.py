from flask import Flask
from flask.blueprints import Blueprint
import config as c
import routes

app = Flask(__name__)

@app.route("/")
def bruh():
    return "Yes and thank you."

# Set debug mode
app.debug = c.DEBUG

# Registers all the routes
for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix=c.APP_ROOT)

app.run(port=c.PORT)