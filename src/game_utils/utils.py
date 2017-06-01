import random
from enum import Enum

from src.game_utils import GRID_SQUARE_SIZE, turtle
from src.game_utils.game_setup import screen
from src.game_utils.point import create_point, Point


class Directions(Enum):
    Left = 0,
    Right = 1,
    Up = 2,
    Down = 3


direction_val = {
    Directions.Left: (-1, 0),
    Directions.Right: (1, 0),
    Directions.Up: (0, 1),
    Directions.Down: (0, -1)
}


def get_random_point():
    """
    Returns a point that's bounded inside the game screen
    """
    # The canvas width, height represent the boundary absolute number not the true size
    width, height = screen.screensize()

    # Pick a random index
    x = get_random_valid_food_coordinate(width)
    y = get_random_valid_food_coordinate(height)
    return create_point(x, y)


def get_random_valid_food_coordinate(dimension_max):
    valid_dimension_max = dimension_max - GRID_SQUARE_SIZE

    # Number of grid squares that can fit in the given dimension
    # 2*w and 2*h represent the real available locations
    grid_count = (2 * valid_dimension_max) // GRID_SQUARE_SIZE

    # Range of valid square center points in the given dimension
    dimension_range = range(-valid_dimension_max, valid_dimension_max, GRID_SQUARE_SIZE)
    random_index = random.randint(1, grid_count - 1)
    return dimension_range[random_index]


def get_next_point(current: Point, direction: Directions):
    """
    Moves from the current location to the next point based on a given direction
    :param current: Current location 
    :param direction: Direction on screen
    :return: next point on screen
    """
    # Unpack the tuples
    dir_x, dir_y = direction_val[direction]

    next_x = current.x + GRID_SQUARE_SIZE * dir_x
    next_y = current.y + GRID_SQUARE_SIZE * dir_y

    return Point(next_x, next_y)


def out_of_screen(point):
    # screensize returns half of the screen size (max abs value for location)
    # as it considers the screen center as 0,
    # and the player moves in the positive and negative range
    cv = screen.getcanvas()
    max_x, max_y = cv.canvwidth, cv.canvheight

    if not_in_range(abs(point.x), max_x) or not_in_range(abs(point.y), max_y):
        return True

    return False


def not_in_range(x, point_range):
    if x < -point_range or x > point_range:
        return True
    return False


def clear_turtle():
    """Clears everything on the screen"""
    turtle.clear()


def kill_game():
    """Closes the game window"""
    screen.bye()


def set_turtle_color_string(color_name: str):
    turtle.fillcolor(color_name.strip())


def set_turtle_color_rgb(r, g, b):
    turtle.fillcolor(r, g, b)
