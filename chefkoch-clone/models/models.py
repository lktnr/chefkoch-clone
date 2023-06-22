from typing import List
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.sql import func


class Recipe(Base):
    __tablename__ = "recipe"

    id: Mapped[int] = mapped_column(primary_key=True)
    creation_time = Column(
        DateTime, default=func.now())
    title: Mapped[str]
    description: Mapped[str]
    duration: Mapped[int]
    difficulty: Mapped[int]
    calories: Mapped[int]

    ingredients: Mapped[List["Ingredient"]
                        ] = relationship(back_populates="recipe")


class Ingredient(Base):
    __tablename__ = "ingredient"

    id: Mapped[int] = mapped_column(primary_key=True)
    recipe_id = mapped_column(ForeignKey("recipe.id"))
    ingredient: Mapped[str]
    weight: Mapped[int]

    recipe: Mapped[Recipe] = relationship(back_populates="ingredients")
