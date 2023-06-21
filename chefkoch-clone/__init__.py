import warnings
from flask import Flask
from sqlalchemy import create_engine
from .models.base import Base
from sqlalchemy.orm import Session
from flask_smorest import Api


app = Flask(__name__)

# sqlalchemy configuration
engine = create_engine(
    "postgresql+psycopg2://root:root@localhost:5432/postgres")

from .models import models  # nopep8, imports tables before create_all()
Base.metadata.create_all(engine)
session = Session(engine)

# flask-smorest configuration and api endpoints setup
app.config["API_TITLE"] = "chefkoch-clone"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_JSON_PATH"] = "api-spec.json"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
api = Api(app)
warnings.filterwarnings(
    "ignore",
    message="Multiple schemas resolved to the name "
)
from . import views  # nopep8
from . import endpoints  # nopep8
