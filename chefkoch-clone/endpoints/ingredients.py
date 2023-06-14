from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.models import Ingredient
import marshmallow as ma
from flask_smorest import Blueprint
from marshmallow_sqlalchemy.fields import Nested


class IngredientSchema(SQLAlchemyAutoSchema):
    recipe = Nested("RecipeSchema", only=("id", "title"))

    class Meta:
        model = Ingredient
        include_relationships = True
        load_instance = True


class IngredientQueryArgsSchema(ma.Schema):
    ingredient = ma.fields.Str()
    weight = ma.fields.Int()


blp = Blueprint(
    'Ingredient',
    __name__,
    url_prefix='/ingredient',
    description="Operations on Ingredients"
)


# @blp.route('/')
# class Members(MethodView):

#     @blp.arguments(RecipeQueryArgsSchema, location='query')
#     @blp.response(200, RecipeSchema(many=True))
#     def get(self, args):
#         """List members"""
#         # TODO: Add birthdate min/max filters
#         recipes = session.execute(select(Recipe))
#         return RecipeSchema(many=True).dump([value for value, in recipes])

#     @blp.etag
#     @blp.arguments(RecipeQueryArgsSchema)
#     @blp.response(201, RecipeSchema)
#     def post(self, new_item):
#         """Add a new member"""
#         try:
#             item = RecipeSchema().load(new_item)
#         except ma.ValidationError as err:
#             return print(err.messages), 400
#         session.add(item)
#         session.commit()
#         return RecipeSchema.dump(item)
