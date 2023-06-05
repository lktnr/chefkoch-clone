import secrets
from flask import Flask
from sqlalchemy import create_engine, select
from .models.base import Base
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap5
from .models.models import Recipe, Ingredient, User
from sqlalchemy.orm import Session


app = Flask(__name__)

foo = secrets.token_urlsafe(16)
app.secret_key = foo
csrf = CSRFProtect(app)

bootstrap = Bootstrap5(app)

engine = create_engine(
    "postgresql+psycopg2://root:root@localhost:5432/postgres")

Base.metadata.create_all(engine)
session = Session(engine)

# Bottom of file
from . import views  # nopep8
