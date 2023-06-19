from .recipies import blp as blp_recipe
from .ingredients import blp as blp_ingredients
from .. import api

api.register_blueprint(blp_recipe)
api.register_blueprint(blp_ingredients)
