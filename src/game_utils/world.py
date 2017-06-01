from src import game_utils
import src.game_utils.function_proxy
from src.game_utils import screen
from src.game_utils.food import Food
from src.game_utils.snake import Snake
from src.game_utils.utils import get_random_point, kill_game


class World:
    """
    Game world:
    - contains all the objects in the game
    - has the screen update handling
    - has game logic handling for each frame
    """

    def __init__(self):
        # game object has a screen, a turtle, a basic snake and a food
        self.artist = game_utils.turtle
        self.artist.up()
        self.artist.speed(0)

        self.snake = Snake()
        self.food = Food(get_random_point())
        self.score = 0
        screen.tracer(0)

        # Can't refactor directions to one functions
        # because of the callback
        screen.onkeypress(self.snake.point_down, "Down")
        screen.onkeypress(self.snake.point_upwards, "Up")
        screen.onkeypress(self.snake.point_left, "Left")
        screen.onkeypress(self.snake.point_right, "Right")
        screen.listen()
        screen.ontimer(self.render_screen, game_utils.REFRESH_INTERVAL // 5)

    def next_frame(self):
        # Clear the screen to avoid drawing overlapping things
        # that's why locating objects and drawing them must be
        # separated
        self.artist.clear()

        # World over, clear all and don't refresh frames
        if self.snake.crashed:
            kill_game()
            return

        # Call protons function if it exists
        if game_utils.function_proxy.proton_frame_logic is not None:
            game_utils.function_proxy.proton_frame_logic()

        # End of frame logic
        self.food.change_state()  # makes the food flash
        screen.ontimer(lambda: self.next_frame(), game_utils.REFRESH_INTERVAL)

        score_str = 'Score: ' + str(self.score)
        src.basic_functions.print_text_to_screen(-350, 270, score_str)

    def render_screen(self):
        # # Rendering updates
        self.food.draw_self()  # show the food and snake
        self.snake.draw_self()
        screen.update()
        screen.ontimer(self.render_screen, 15)
