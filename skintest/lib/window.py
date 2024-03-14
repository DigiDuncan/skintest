from arcade import Sprite, Window
from arcade import draw_polygon_filled

from skintest.lib.skin import skin
from skintest.lib.utils import get_triangle_points


class SkinWindow(Window):
    def __init__(self):
        super().__init__(1280, 720)

        self.a = Sprite(skin.textures.icon,
                        center_x=500, center_y=200)

    def on_draw(self):
        self.clear(skin.colors.primary)
        self.a.draw()
        draw_polygon_filled(get_triangle_points(skin.positions.triangle, 100), skin.colors.secondary)
