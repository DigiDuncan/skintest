from pathlib import Path
import tomllib
from typing import Self, TypeVar, Sequence
import importlib.resources as pkg_resources

from benedict import benedict

from arcade import Texture, load_texture
from arcade.types import Color, Point

import skintest.data.skin

T = TypeVar("T")


def get_texture(root: Path, path: str) -> Texture:
    fullpath = root / path
    return load_texture(fullpath)


def get_color(i: Sequence) -> Color:
    return Color(*i)


class_map: dict[T, callable] = {
    Texture: get_texture,
    Color: get_color
}

type_map: dict[str, T] = {
    "colors.primary": Color,
    "colors.secondary": Color,
    "textures.icon": Texture,
    "positions.triangle": Point
}


class Skin(benedict):
    def __init__(self, data: dict = None, *args, **kwargs):
        data = {} if data is None else data
        super().__init__(data, *args, **kwargs)

    @classmethod
    def from_data(cls, path: Path, data: dict) -> Self:
        data = benedict(data)
        for key, value in type_map.items():
            if value == Texture:
                data[key] = get_texture(path, data[key])
            elif value in class_map:
                data[key] = class_map[value](data[key])
        return cls(data)

    @classmethod
    def from_toml(cls, path: Path) -> Self:
        with open(path / "skin.toml") as f:
            tom = tomllib.loads(f.read())
        return cls.from_data(path, tom)

    @classmethod
    def compose(cls, root: Path, paths: list[str]) -> Self:
        composed = {}
        for p in paths:
            path = root / p
            with open(path / "skin.toml") as f:
                tom = tomllib.loads(f.read())
            composed |= tom
        return cls.from_data(root, composed)


with pkg_resources.path(skintest.data, "skin") as p:
    skin = Skin.from_toml(p)
