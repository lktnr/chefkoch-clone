from flask.views import MethodView
from ..models.models import Recipe, Ingredient
from sqlalchemy import select
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import marshmallow as ma
from marshmallow_sqlalchemy.fields import Nested
from flask_smorest import Blueprint, abort
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .. import session
from .ingredients import IngredientQueryArgsSchema


class RecipeSchema(SQLAlchemyAutoSchema):
    ingredients = ma.fields.List(Nested(
        "IngredientSchema", exclude=("recipe",)))

    class Meta:
        model = Recipe
        include_relationships = True
        load_instance = True


class RecipeQueryArgsSchema(ma.Schema):
    title = ma.fields.Str()
    description = ma.fields.Str()
    duration = ma.fields.Int()
    difficulty = ma.fields.Int()
    calories = ma.fields.Int()
    ingredients = ma.fields.List(ma.fields.Nested(
        IngredientQueryArgsSchema(exclude=("recipe_id",))))

    @ma.post_load
    def create_ingredients(self, data, **kwargs):
        if "ingredients" in data:
            data["ingredients"] = [Ingredient(**value)
                                   for value in data["ingredients"]]
        return data


blp = Blueprint(
    'Recipe',
    __name__,
    url_prefix='/recipe',
    description="Operations on recepies"
)


def deleteIngredients_recipeIsNull():
    ingredientsWithNoRecipe = session.execute(
        select(Ingredient).where(Ingredient.recipe == None))
    for ingredients, in ingredientsWithNoRecipe:
        session.delete(ingredients)


@blp.route('/')
class Recepies(MethodView):

    @blp.arguments(RecipeQueryArgsSchema(exclude=("ingredients",)), location='query')
    @blp.response(200, RecipeSchema(many=True))
    def get(self, recipe):
        """Filter all recipes"""
        query = select(Recipe)
        if "title" in recipe:
            query = query.where(Recipe.title.ilike(f'%{recipe["title"]}%'))
        if "description" in recipe:
            query = query.where(Recipe.description.contains(
                f'%{recipe["description"]}%'))
        if "duration" in recipe:
            query = query.where(Recipe.duration <= recipe["duration"])
        if "difficulty" in recipe:
            query = query.where(Recipe.difficulty <= recipe["difficulty"])
        if "calories" in recipe:
            query = query.where(Recipe.calories <= recipe["calories"])
        recipes = session.execute(query)
        return [value for value, in recipes]

    @blp.arguments(RecipeQueryArgsSchema)
    @blp.response(201, RecipeSchema)
    def post(self, new_recipe):
        """Add a new recipe"""
        recipe = Recipe(**new_recipe)
        session.add(recipe)

        try:
            session.commit()
        except:
            session.rollback()
            abort(500, message="Something went wrong")
        return recipe


@blp.route('/<int:recipe_id>')
class RecepiesById(MethodView):

    @blp.response(200, RecipeSchema)
    def get(self, recipe_id):
        """Get a recipe"""
        recipe = session.get(Recipe, recipe_id)

        if recipe == None:
            abort(404, message="Object not found")
        return recipe

    @blp.arguments(RecipeQueryArgsSchema)
    @blp.response(200, RecipeSchema)
    def put(self, new_recipe, recipe_id):
        """Update an existing recipe"""
        recipe = session.get(Recipe, recipe_id)
        if recipe == None:
            abort(404, message="Object not found")
        recipe.title = new_recipe["title"]
        recipe.description = new_recipe["description"]
        recipe.duration = new_recipe["duration"]
        recipe.difficulty = new_recipe["difficulty"]
        recipe.calories = new_recipe["calories"]
        recipe.ingredients = new_recipe["ingredients"]
        deleteIngredients_recipeIsNull()

        try:
            session.commit()
        except:
            session.rollback()
            abort(500, message="Something went wrong")
        return recipe

    @blp.response(204)
    def delete(self, recipe_id):
        """Delete a recipe"""
        recipe = session.get(Recipe, recipe_id)
        if recipe == None:
            abort(404, message="Object not found")
        session.delete(recipe)
        deleteIngredients_recipeIsNull()

        try:
            session.commit()
        except:
            session.rollback()
            abort(500, message="Something went wrong")
