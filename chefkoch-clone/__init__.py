from flask import Flask
from sqlalchemy import create_engine, select
from .models.base import Base
from .models.models import Recipe, Ingredient, User
from sqlalchemy.orm import Session
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

engine = create_engine(
    "postgresql+psycopg2://root:root@localhost:5432/postgres")

Base.metadata.create_all(engine)
session = Session(engine)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
# end swagger specific ###s

# Bottom of file
from . import views  # nopep8
