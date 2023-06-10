from .recipies import blp as blp_recipe
from .. import api

api.register_blueprint(blp_recipe)
