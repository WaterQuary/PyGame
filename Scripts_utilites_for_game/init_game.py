import pygame as pg
from Game.GameMenu import Show
def start_games():
    pg.init()

    start = Show()
    start.show_in_game()

    pg.quit()