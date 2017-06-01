from src.game_utils import *
from src.game_utils.game_setup import game_world
from src.game_utils.utils import turtle, clear_turtle, kill_game, get_random_point, out_of_screen, get_next_point
from src.game_utils.square import create_square


"""
    This File has all the functions you will need to build your own snake game, 
    Read all functions documentations to understand what they can do, 
    Good Luck!
"""


def change_food_location(point):
    """
    This function changes the location the food is spawned
    :param point: the point representing the next location it can be made with Point(x,y)
    where x and y are the coordinates of the new location
    """
    game_world.food.change_location(point)


def get_food_position():
    """
    This function gets the location of the food as a point
    :return: a Point which has an x and a y coordinates
    to get its coordinates:
        point = get_food_position()
        point.x # to get the x coordinate
        point.y # to get the y coordinate
    """
    return game_world.food.position


def calculate_snake_next_position():
    """
        This function gets the location of the next position of the snake as a point
        :return: a Point which has an x and a y coordinates
        to get its coordinates:
            point = calculate_snake_next_position()
            point.x # to get the x coordinate
            point.y # to get the y coordinate
        """
    return game_world.snake.next_position


def get_snake():
    """
        This function returns the snake, this snake has properties and functions which can be used like this:
        snake = get_snake()
        snake.head_position  # which contains the head of the snake,
        snake.next_position  # which contains the next position of the snake
        snake.move_direction # which contains the direction the snake is moving
        snake.move_head_to_next_location() # moves the head of the snake to next_position

    """
    return game_world.snake


def get_point_in_direction(point, direction):
    """
    Gets the next point the direction given, 
    Example:
    p = Point(0,0)
    get_point_in_direction(p,Directions.Right) # returns Point(1,0)
    :param point: the given starting point 
    :param direction: the required direction to move the point into
    :return: the calculated next point
    """
    return get_next_point(point, direction)


def point_snake_up():
    """Changes the direction of the snake, but doesn't move it"""
    game_world.snake.point_upwards()


def point_snake_down():
    """Changes the direction of the snake, but doesn't move it"""
    game_world.snake.point_down()


def point_snake_left():
    """Changes the direction of the snake, but doesn't move it"""
    game_world.snake.point_left()


def point_snake_right():
    """Changes the direction of the snake, but doesn't move it"""
    game_world.snake.point_right()


def move_snake_head_to_next():
    """Moves the snake to the direction it's pointing to"""
    game_world.snake.move_head_to_next_location()


def clear_screen():
    """
    This function clears the screen
    """
    clear_turtle()


def get_snake_body():
    """
    Returns the list of squares forming the body of the snake,
     where the last element in it is the head of the snake
    """
    return game_world.snake.body


def add_next_position_to_snake_body(snake):
    """
    Adds the next position to snake body
    :param snake
    """
    snake.body.append(create_square(snake.next_position.x, snake.next_position.y))


def game_over():
    """Ends the game and closes the window"""
    kill_game()


def set_color_string(color):
    """
    This function changes the color of the snake and the food.
    :param color: a string that represents the color, example: 'blue'
    """
    turtle.fillcolor(color)


def set_game_speed(interval):
    """
        This function changes the speed of the game
        :param interval: an int that slows the speed when its larger
    """
    set_interval(interval)


def increase_score():
    """
    increases the score of the game.
    """
    game_world.score += 1


def reset_score():
    """
    resets the score of the game.
    """
    game_world.score = 0


def print_text_to_screen(x, y, text):
    """
    print a string on the screen
    :param x: an int representing the x coordinate of the position of text
    :param y: an int representing the y coordinate of the position of text
    :param text: a string representing the text to be printed on screen 
    """
    turtle.setpos((x, y))
    turtle.write(text, move='False', align='center', font=('Arial', 16, 'normal'))


def is_out_of_screen(point):
    """
    Checks if a given point is out of the screen,

    Example:
     p = Point(20,20)
     is_out_of_screen(point) # returns True

    :param point: A Point that has x and y coordinates
    :return returns a Boolean, A True or a False
    """
    return out_of_screen(point)


def random_point():
    """
    Gets a random point on the screen
    :return: returns a Point(x,y) on the screen
    """
    return get_random_point()
