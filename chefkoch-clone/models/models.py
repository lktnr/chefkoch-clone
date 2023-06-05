import datetime
from typing import Dict, List
from typing import Optional
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    creation_time: datetime = Column(DateTime, default=datetime.datetime.now)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    recepies: Mapped[List["Recipe"]] = relationship(back_populates="user")

    # Replace later
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Recipe(Base):
    __tablename__ = "recipe"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(ForeignKey("user.id"))
    creation_time: datetime = Column(DateTime, default=datetime.datetime.now)
    title: Mapped[str]
    description: Mapped[str]
    duration: Mapped[int]
    difficulty: Mapped[int]
    calories: Mapped[int]

    ingredients: Mapped[List["Ingredient"]
                        ] = relationship(back_populates="recipe")
    user: Mapped[User] = relationship(back_populates="recepies")

    # Replace later
    def __repr__(self) -> str:
        return f"Recipe(id={self.id!r}, title={self.title!r})"


class Ingredient(Base):
    __tablename__ = "ingredient"

    id: Mapped[int] = mapped_column(primary_key=True)
    recipe_id = mapped_column(ForeignKey("recipe.id"))
    ingredient: Mapped[str]
    weight: Mapped[int]

    recipe: Mapped[Recipe] = relationship(back_populates="ingredients")
