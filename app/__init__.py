from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

from app import controllers

SWAGGER_URL = '/swagger'
API_URL = 'http://petstore.swagger.io/v2/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
