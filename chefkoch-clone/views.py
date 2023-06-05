from flask import flash, render_template, redirect, request
from sqlalchemy import select
from .models.models import Ingredient, Recipe
from .models.base import Base
from . import app, session, engine


@app.route('/')
def home():
    return render_template('home.html')
