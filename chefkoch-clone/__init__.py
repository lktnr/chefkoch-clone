from flask import Flask
from sqlalchemy import create_engine
from .models.base import Base
from sqlalchemy.orm import Session
from flask_smorest import Api


app = Flask(__name__)

# sqlalchemy
engine = create_engine(
    "postgresql+psycopg2://root:root@localhost:5432/postgres")

from .models.models import Recipe, Ingredient, User  # nopep8, imports tables before create_all()
Base.metadata.create_all(engine)
session = Session(engine)

# flask-smorest
app.config["API_TITLE"] = "chefkoch-clone"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_JSON_PATH"] = "api-spec.json"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
api = Api(app)


# Bottom of file
from . import views  # nopep8
from . import endpoints  # nopep8
