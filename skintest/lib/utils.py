from arcade.types import Point


def get_triangle_points(center: Point, size: float) -> list[Point]:
    top = center[1] + size / 2
    bottom = center[1] - size / 2
    left = center[0] - size / 2
    right = center[0] + size / 2
    return [
        (center[0], top),
        (left, bottom),
        (right, bottom)
    ]
