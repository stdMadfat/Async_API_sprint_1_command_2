from decimal import Decimal
from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class Genre(BaseModel):
    uuid: UUID = Field(..., description="Уникальный идентификатор жанра")
    name: str = Field(
        ..., min_length=1, max_length=50, description="Название жанра"
    )
    description: str | None = Field(None, description="Описание жанра")


class GenreBase(BaseModel):
    """
    Модель для представления жанра.
    """
    id: UUID = Field(
        ...,
        description="Уникальный идентификатор жанра",
        serialization_alias='uuid'
    )
    name: str = Field(
        ..., min_length=1, max_length=50, description="Название жанра"
    )


class PersonBase(BaseModel):
    """
    Базовая модель для представления информации о персоне.
    """
    id: UUID = Field(
        ...,
        description="Уникальный идентификатор персоны",
        serialization_alias='uuid'
    )
    full_name: str = Field(
        ..., min_length=1, max_length=150, description="Полное имя персоны"
    )


class Film(BaseModel):
    """
    Модель для представления информации о фильме.
    """
    id: UUID = Field(
        ...,
        description="Уникальный идентификатор фильма",
        serialization_alias="uuid"
    )
    title: str = Field(
        ..., min_length=1, max_length=255, description="Название фильма"
    )
    description: str = Field(..., description="Описание фильма")
    genre: list[GenreBase] = Field(
        default_factory=list, description="Список жанров фильма"
    )
    actors: list[PersonBase] = Field(
        default_factory=list, description="Список актёров фильма"
    )
    writers: list[PersonBase] = Field(
        default_factory=list, description="Список сценаристов фильма"
    )
    directors: list[PersonBase] = Field(
        default_factory=list, description="Список режиссёров фильма"
    )
    imdb_rating: Decimal = Field(
        ..., ge=1, le=10, description="Рейтинг фильма по версии IMDb"
    )


class Person(BaseModel):
    """
    Модель для представления информации о персоне.
    """
    uuid: str
    full_name: str
    films: List[Film] = Field(default_factory=list)
