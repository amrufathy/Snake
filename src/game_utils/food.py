from src.game_utils.square import draw_square
from src.game_utils.utils import get_random_point


class Food:
    """Food representation in game"""

    def __init__(self, point):
        self.position = point
        self.is_blinking = True

    def __repr__(self):
        """
        What to be printed in debug mode
        :return: 
        """
        return str(self.position)

    def __str__(self):
        """
        What to be returned when the Point is converted to a string
        :return: 
        """
        return self.__repr__()

    def change_location(self, point):
        # I haven't programmed it to spawn outside the snake's body yet
        self.position = point

    def draw_self(self):
        # similar to the Square draw_square, but blinks on and off
        if self.is_blinking:
            draw_square(self.position)

    def change_state(self):
        # controls the blinking
        self.is_blinking = not self.is_blinking
