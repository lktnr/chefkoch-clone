from flask.views import MethodView
from ..models.models import Recipe
from sqlalchemy import select
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import marshmallow as ma
from flask_smorest import Blueprint, abort, Page
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, auto_field
from .. import api, session


class RecipeSchema(SQLAlchemyAutoSchema):
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


blp = Blueprint(
    'Recipe',
    __name__,
    url_prefix='/recipe',
    description="Operations on recepies"
)


@blp.route('/')
class Members(MethodView):

    @blp.arguments(RecipeQueryArgsSchema, location='query')
    @blp.response(200, RecipeSchema(many=True))
    def get(self, args):
        """List members"""
        # TODO: Add birthdate min/max filters
        recipes = session.execute(select(Recipe))
        return RecipeSchema(many=True).dump([value for value, in recipes])

    # @blp.etag
    # @blp.arguments(MemberSchema)
    # @blp.response(201, MemberSchema)
    # def post(self, new_item):
    #     """Add a new member"""
    #     item = Member(**new_item)
    #     db.session.add(item)
    #     db.session.commit()
    #     return item


# @blp.route('/<uuid:item_id>')
# class MembersById(MethodView):

#     @blp.etag
#     @blp.response(200, MemberSchema)
#     def get(self, item_id):
#         """Get member by ID"""
#         return Member.query.get_or_404(item_id)

#     @blp.etag
#     @blp.arguments(MemberSchema)
#     @blp.response(200, MemberSchema)
#     def put(self, new_item, item_id):
#         """Update an existing member"""
#         item = Member.query.get_or_404(item_id)
#         blp.check_etag(item, MemberSchema)
#         MemberSchema().update(item, new_item)
#         db.session.add(item)
#         db.session.commit()
#         return item

#     @blp.etag
#     @blp.response(204)
#     def delete(self, item_id):
#         """Delete a member"""
#         item = Member.query.get_or_404(item_id)
#         blp.check_etag(item, MemberSchema)
#         db.session.delete(item)
#         db.session.commit()
