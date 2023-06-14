import datetime
from typing import List
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    # default does not work when manually creating in pgadmin
    creation_time = Column(
        DateTime, default=func.now)
    userName: Mapped[str] = mapped_column(String(30))
    password: Mapped[str]

    recepies: Mapped[List["Recipe"]] = relationship(back_populates="user")


class Recipe(Base):
    __tablename__ = "recipe"

    id: Mapped[int] = mapped_column(primary_key=True)
    creation_time = Column(
        DateTime, default=func.now())
    user_id = mapped_column(ForeignKey("user.id"))
    title: Mapped[str]
    description: Mapped[str]
    duration: Mapped[int]
    difficulty: Mapped[int]
    calories: Mapped[int]

    ingredients: Mapped[List["Ingredient"]
                        ] = relationship(back_populates="recipe")
    user: Mapped[User] = relationship(back_populates="recepies")


class Ingredient(Base):
    __tablename__ = "ingredient"

    id: Mapped[int] = mapped_column(primary_key=True)
    recipe_id = mapped_column(ForeignKey("recipe.id"))
    ingredient: Mapped[str]
    weight: Mapped[int]

    recipe: Mapped[Recipe] = relationship(back_populates="ingredients")
