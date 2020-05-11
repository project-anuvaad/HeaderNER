from flask import Flask
from flask.blueprints import Blueprint
from flask_cors import CORS
import routes
import config

ner_app  = Flask(__name__)

if config.ENABLE_CORS:
    cors    = CORS(ner_app, resources={r"/api/*": {"origins": "*"}})

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        ner_app.register_blueprint(blueprint, url_prefix=config.API_URL_PREFIX)

if __name__ == "__main__":
    ner_app.run(host=config.HOST, port=config.PORT, debug=True)
