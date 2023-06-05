from flask import flash, render_template, redirect, request
from sqlalchemy import select
from .forms.forms import IngredientForm, RecipeForm
from .models.models import Ingredient, Recipe
from .models.base import Base
from . import app, session, engine, csrf


@app.route('/')
def home():
    recipes = session.execute(select(Recipe))
    return render_template('home.html', recipes=recipes)


@app.route('/new', methods=['GET', 'POST'])
@csrf.exempt
def new():
    form = RecipeForm()
    if form.validate_on_submit():
        return redirect("/new/ingredients")
    return render_template('recipeForm.html', form=form)


@app.route('/new/ingredients', methods=['GET', 'POST'])
@csrf.exempt
def newIngredients():
    form = IngredientForm()
    if form.validate_on_submit():
        if request.form['addIngredient'] == 'Add additonal ingredient':
            return redirect("/new/ingredients")
        else:
            flash('You\'ve uploaded a new recipe!')
            return redirect("/")
    return render_template('recipeForm.html', form=form)
