"""
    Game entry point, you don't need to modify this file

    What is simply does is:
    - Create the game world
    - Renders the first game frame
    - Waits a little bit
    - Starts the game
"""
import time

from src.game_utils import screen
from src.game_utils.world import World

game_world = World()


def run_game_loop():
    game_world.next_frame()
    # delay before starting the game,
    # it's rude to directly start the game once it shows up
    time.sleep(0.5)
    screen.mainloop()
