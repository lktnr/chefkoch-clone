from flask import flash, render_template, redirect, request
from sqlalchemy import select
from . import app, session, engine


# @app.route('/')
# def home():
#     return render_template('home.html')
