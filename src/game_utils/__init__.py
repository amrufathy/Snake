"""Setup the global variables"""
from turtle import Turtle

GRID_SQUARE_SIZE = 20
REFRESH_INTERVAL = 1000
turtle = Turtle(visible=False)
screen = turtle.screen


def set_interval(interval):
    global REFRESH_INTERVAL
    REFRESH_INTERVAL = interval
