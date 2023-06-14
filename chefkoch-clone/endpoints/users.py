from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.models import User
import marshmallow as ma
from flask_smorest import Blueprint


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True


class UserQueryArgsSchema(ma.Schema):
    username = ma.fields.Str()


blp = Blueprint(
    'User',
    __name__,
    url_prefix='/user',
    description="Operations on users"
)
