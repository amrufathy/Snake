import src.game_utils.function_proxy as check
from src.basic_functions import *

"""
    This file is the one you'll be working on 
    read the documentation of the functions to know 
    what it must be able to do.
"""


# TODO:: implement this
def move_snake():
    """
    This function controls how the snake moves
    """
    raise NotImplementedError("Implement move_snake() function then remove the line starting with raise")


# TODO:: implement this
def grow_snake():
    """
    This function is responsible for growing the snake when it eats food
    """
    raise NotImplementedError("Implement grow_snake() function then remove the line starting with raise")


# TODO:: implement this
def frame_logic():  # Don't change the name of this function
    """
        This function now only changes the food location each frame into a random location which is obviously wrong :D, 
        add your own code that defines what happens when each frame is drawn, it should basically move the snake and 
        update the score and the food. 
        a simple code example: 
            move_snake()
            if (get_food_position() == calculate_snake_next_position()):
                change_food_location(random_point())
                grow_snake()
    """
    change_food_location(random_point())


# TODO:: (optional) add to this function if needed
def setup():  # Don't change the name of this function
    """
    This function contains the game setup logic, add any code here that you want to 
    execute before the game is loaded  
    """
    # change speed
    set_game_speed(180)
    # change color
    set_color_string("blue")


# DO NOT CHANGE THIS FUNCTION
def submit_your_functions():
    check.proton_frame_logic = frame_logic
