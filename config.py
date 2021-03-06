from random import choice

"""Можно редактировать"""

background_color: str = "white"
borders_color: str = "#3c3c3c"
second_color: str = "#666666"
cube_colors: list = ["#fff7b3", "#ff7777",
                     "#ffc1b3", "#ffb3f0",
                     "#b8b3ff", "#b3ffc9"]

start_speed: int = 750
max_speed: int = 150
speed_step: int = 50

width: int = 10
height: int = 14
size: int = 50

borders: int = size // 10
gap: int = 1

font: str = "opensans"
font_size: int = size * 4 // 5


"""Не стоит редактировать"""

margin: int = size * 5
screen_width: int = size * max(width, 5)
screen_height: int = size * max(height, 5) + margin


def generate_figure() -> set:
    """Figure generation for tetris"""
    coords = {(0, 0)}
    while len(coords) < 4:
        base = choice(list(coords))
        if choice([0, 1]):
            new_coords = base[0] + 1, base[1]
        else:
            new_coords = base[0], base[1] + 1
        coords.add(new_coords)
    return coords
