from typing import Optional
from flask_wtf import FlaskForm
from ..models.models import Recipe, Ingredient
from wtforms_alchemy import ModelForm, ModelFieldList
from wtforms.fields import FormField, SubmitField


class IngredientForm(ModelForm, FlaskForm):
    class Meta:
        model = Ingredient

    submit = SubmitField('Submit')
    addIngredient = SubmitField('Add additonal ingredient')


class RecipeForm(ModelForm, FlaskForm):
    class Meta:
        model = Recipe

    # ingredients = ModelFieldList(
    #     FormField(IngredientForm), min_entries=10)

    submit = SubmitField('Submit')
    # addIngredient = SubmitField('Add Ingredient')
