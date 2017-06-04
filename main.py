from src.game_utils.game_setup import *
from src.tasks import submit_your_functions
from src.tasks import setup

"""
    This file is the one you will use to run the game. don't mind the code here. 
    Check basic_functions.py to know what tools you have and
    tasks.py to know what you'll have to do.
"""


def main():
    # setup code before the game starts
    setup()
    # Do all other setup before game loop
    # Don't modify the below code
    submit_your_functions()
    run_game_loop()


main()
