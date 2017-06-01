from src import game_utils
import src.game_utils.function_proxy
from src.game_utils.square import *
from src.game_utils.utils import *


class Snake:
    def __init__(self):
        """
        Snake setup
        """
        self.head_position = create_point(GRID_SQUARE_SIZE, 0)  # keeps track of where it needs to go next
        self.direction = Directions.Right
        # body is a queue of squares
        self.body = [create_square(0, 0)]

        self.move_direction = Directions.Right
        self.crashed = False  # Used to indicate end of game
        self.next_position = get_next_point(self.head_position, self.move_direction)

    def move(self):
        """
        Snake motion
        """
        if game_utils.function_proxy.proton_move_snake is not None:
            game_utils.function_proxy.proton_move_snake()

    def point_upwards(self):  # pretty obvious what these do
        if self.move_direction == Directions.Down:
            return
        self.move_direction = Directions.Up

    def point_left(self):
        if self.move_direction == Directions.Right:
            return
        self.move_direction = Directions.Left

    def point_right(self):
        if self.move_direction == Directions.Left:
            return
        self.move_direction = Directions.Right

    def point_down(self):
        if self.move_direction == Directions.Up:
            return
        self.move_direction = Directions.Down

    def move_head_to_next_location(self):
        # Calculate the next position
        self.head_position = self.next_position
        self.next_position = get_next_point(self.head_position, self.move_direction)

    def grow(self):
        if game_utils.function_proxy.proton_grow_snake is not None:
            game_utils.function_proxy.proton_grow_snake()

    def draw_self(self):
        """
        Draws the snake on the screen
        :return: 
        """
        for square in self.body:
            draw_square(square)
