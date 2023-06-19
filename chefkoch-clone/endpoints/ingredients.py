from flask.views import MethodView
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.models import Ingredient, Recipe
import marshmallow as ma
from flask_smorest import Blueprint, abort
from marshmallow_sqlalchemy.fields import Nested
from .. import session


class IngredientSchema(SQLAlchemyAutoSchema):
    recipe = Nested("RecipeSchema", only=("id", "title"))

    class Meta:
        model = Ingredient
        include_relationships = True
        load_instance = True


def validate_recipe_exists(recipe_id):
    recipe = session.get(Recipe, recipe_id)
    if recipe == None:
        raise ma.ValidationError("No recipe for id found.")


class IngredientQueryArgsSchema(ma.Schema):
    ingredient = ma.fields.Str()
    weight = ma.fields.Int()
    recipe_id = ma.fields.Int(validate=validate_recipe_exists)


blp = Blueprint(
    'Ingredient',
    __name__,
    url_prefix='/ingredient',
    description="Operations on Ingredients"
)


@blp.route('/')
class Recepies(MethodView):

    @blp.arguments(IngredientQueryArgsSchema)
    @blp.response(201, IngredientSchema)
    def post(self, new_ingredient):
        """Add a new ingrendient"""
        ingredient = Ingredient(**new_ingredient)
        session.add(ingredient)
        try:
            session.commit()
        except:
            session.rollback()
            abort(500, message="Something went wrong")
        return ingredient


@blp.route('/<int:ingredient_id>')
class RecepiesById(MethodView):

    @blp.response(200, IngredientSchema)
    def get(self, ingredient_id):
        """Get an ingredient"""
        ingredient = session.get(Ingredient, ingredient_id)
        if ingredient == None:
            abort(404, message="Object not found")
        return ingredient

    @blp.arguments(IngredientQueryArgsSchema)
    @blp.response(200, IngredientSchema)
    def put(self, new_ingredient, ingredient_id):
        """Update an existing ingredient"""
        ingredient = session.get(Ingredient, ingredient_id)
        if ingredient == None:
            abort(404, message="Object not found")
        ingredient.ingredient = new_ingredient["ingredient"]
        ingredient.weight = new_ingredient["weight"]
        ingredient.recipe_id = new_ingredient["recipe_id"]

        try:
            session.commit()
        except:
            session.rollback()
            abort(500, message="Something went wrong")
        return ingredient

    @blp.response(204)
    def delete(self, ingredient_id):
        """Delete a ingredient"""
        recipe = session.get(Ingredient, ingredient_id)
        if recipe == None:
            abort(404, message="Object not found")
        session.delete(recipe)
        try:
            session.commit()
        except:
            session.rollback()
            abort(500, message="Something went wrong")
